// Fill out your copyright notice in the Description page of Project Settings.

using UnrealBuildTool;
using System.Collections.Generic;

public class RoboWorld_BP22Target : TargetRules
{
	public RoboWorld_BP22Target(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;

		ExtraModuleNames.AddRange( new string[] { "RoboWorld_BP22" } );
	}
}
