def warmup_decay_schedule(base_lr: float, warmup_steps: int, total_steps: int, current_step: int) -> float:
    if current_step<warmup_steps:
        return base_lr*(current_step/warmup_steps)
    elif current_step>= warmup_steps:
        return base_lr*((total_steps-current_step)/(total_steps-warmup_steps))