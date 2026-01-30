from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class LatestAiDevelopment():
    """LatestAiDevelopment crew - Multi-channel content generation pipeline"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    # ==================== AGENTS ====================
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            tools=[SerperDevTool()],
            allow_delegation=True
        )
    
    @agent
    def content_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['content_strategist'],
            verbose=True,
            tools=[SerperDevTool()],
            allow_delegation=True
        )

    @agent
    def visual_producer(self) -> Agent:
        return Agent(
            config=self.agents_config['visual_producer'],
            verbose=True,
            allow_delegation=True
        )
    
    @agent
    def multimedia_producer(self) -> Agent:
        return Agent(
            config=self.agents_config['multimedia_producer'],
            verbose=True,
            allow_delegation=True
        )
    
    # ==================== TASKS ====================
    
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_and_reporting_task'],  # Match YAML name
            agent=self.research_analyst()  # Assign agent
        )
    
    @task
    def content_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_strategy_task'],  # Match YAML name
            agent=self.content_strategist(),
            context=[self.research_task()]  # Dependencies
        )
    
    @task
    def visual_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['visual_content_task'],  # Match YAML name
            agent=self.visual_producer(),
            context=[self.research_task(), self.content_creation_task()]
        )
    
    @task
    def multimedia_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['multimedia_production_task'],  # Match YAML name
            agent=self.multimedia_producer(),
            context=[self.research_task(), self.content_creation_task()]
        )
    
    @task
    def campaign_integration_task(self) -> Task:
        return Task(
            config=self.tasks_config['campaign_integration_task'],  # Match YAML name
            agent=self.content_strategist(),
            context=[
                self.content_creation_task(),
                self.visual_content_task(),
                self.multimedia_content_task()
            ]
        )
    
    # ==================== CREW ====================
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential, 
            verbose=True,
            memory=True,
            share_crew=True
        )