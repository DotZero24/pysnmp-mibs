_T='etsysNacApplianceMIBGroup'
_S='etsysNacApplConnectedAgents'
_R='etsysNacApplIPResolutionTimeouts'
_Q='etsysNacApplIPResolutionFailures'
_P='etsysNacApplContactLostSwitches'
_O='etsysNacApplCaptivePortalRequests'
_N='etsysNacApplAssessmentRequests'
_M='etsysNacApplAuthenticationUnknownTypes'
_L='etsysNacApplAuthenticationDroppedPackets'
_K='etsysNacApplAuthenticationBadRequests'
_J='etsysNacApplAuthenticationMalformedRequests'
_I='etsysNacApplAuthenticationDuplicateRequests'
_H='etsysNacApplAuthenticationInvalidRequests'
_G='etsysNacApplRadiusChallenges'
_F='etsysNacApplAuthenticationFailures'
_E='etsysNacApplAuthenticationSuccesses'
_D='etsysNacApplAuthenticationRequests'
_C='read-only'
_B='ENTERASYS-NAC-APPLIANCE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysNacApplianceMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,73))
if mibBuilder.loadTexts:etsysNacApplianceMIB.setRevisions(('2010-03-09 13:03',))
_EtsysNacApplianceObjects_ObjectIdentity=ObjectIdentity
etsysNacApplianceObjects=_EtsysNacApplianceObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,73,1))
_EtsysNacApplAuthenticationRequests_Type=Counter64
_EtsysNacApplAuthenticationRequests_Object=MibScalar
etsysNacApplAuthenticationRequests=_EtsysNacApplAuthenticationRequests_Object((1,3,6,1,4,1,5624,1,2,73,1,1),_EtsysNacApplAuthenticationRequests_Type())
etsysNacApplAuthenticationRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplAuthenticationRequests.setStatus(_A)
_EtsysNacApplAuthenticationSuccesses_Type=Counter64
_EtsysNacApplAuthenticationSuccesses_Object=MibScalar
etsysNacApplAuthenticationSuccesses=_EtsysNacApplAuthenticationSuccesses_Object((1,3,6,1,4,1,5624,1,2,73,1,2),_EtsysNacApplAuthenticationSuccesses_Type())
etsysNacApplAuthenticationSuccesses.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplAuthenticationSuccesses.setStatus(_A)
_EtsysNacApplAuthenticationFailures_Type=Counter64
_EtsysNacApplAuthenticationFailures_Object=MibScalar
etsysNacApplAuthenticationFailures=_EtsysNacApplAuthenticationFailures_Object((1,3,6,1,4,1,5624,1,2,73,1,3),_EtsysNacApplAuthenticationFailures_Type())
etsysNacApplAuthenticationFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplAuthenticationFailures.setStatus(_A)
_EtsysNacApplRadiusChallenges_Type=Counter64
_EtsysNacApplRadiusChallenges_Object=MibScalar
etsysNacApplRadiusChallenges=_EtsysNacApplRadiusChallenges_Object((1,3,6,1,4,1,5624,1,2,73,1,4),_EtsysNacApplRadiusChallenges_Type())
etsysNacApplRadiusChallenges.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplRadiusChallenges.setStatus(_A)
_EtsysNacApplAuthenticationInvalidRequests_Type=Counter64
_EtsysNacApplAuthenticationInvalidRequests_Object=MibScalar
etsysNacApplAuthenticationInvalidRequests=_EtsysNacApplAuthenticationInvalidRequests_Object((1,3,6,1,4,1,5624,1,2,73,1,5),_EtsysNacApplAuthenticationInvalidRequests_Type())
etsysNacApplAuthenticationInvalidRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplAuthenticationInvalidRequests.setStatus(_A)
_EtsysNacApplAuthenticationDuplicateRequests_Type=Counter64
_EtsysNacApplAuthenticationDuplicateRequests_Object=MibScalar
etsysNacApplAuthenticationDuplicateRequests=_EtsysNacApplAuthenticationDuplicateRequests_Object((1,3,6,1,4,1,5624,1,2,73,1,6),_EtsysNacApplAuthenticationDuplicateRequests_Type())
etsysNacApplAuthenticationDuplicateRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplAuthenticationDuplicateRequests.setStatus(_A)
_EtsysNacApplAuthenticationMalformedRequests_Type=Counter64
_EtsysNacApplAuthenticationMalformedRequests_Object=MibScalar
etsysNacApplAuthenticationMalformedRequests=_EtsysNacApplAuthenticationMalformedRequests_Object((1,3,6,1,4,1,5624,1,2,73,1,7),_EtsysNacApplAuthenticationMalformedRequests_Type())
etsysNacApplAuthenticationMalformedRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplAuthenticationMalformedRequests.setStatus(_A)
_EtsysNacApplAuthenticationBadRequests_Type=Counter64
_EtsysNacApplAuthenticationBadRequests_Object=MibScalar
etsysNacApplAuthenticationBadRequests=_EtsysNacApplAuthenticationBadRequests_Object((1,3,6,1,4,1,5624,1,2,73,1,8),_EtsysNacApplAuthenticationBadRequests_Type())
etsysNacApplAuthenticationBadRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplAuthenticationBadRequests.setStatus(_A)
_EtsysNacApplAuthenticationDroppedPackets_Type=Counter64
_EtsysNacApplAuthenticationDroppedPackets_Object=MibScalar
etsysNacApplAuthenticationDroppedPackets=_EtsysNacApplAuthenticationDroppedPackets_Object((1,3,6,1,4,1,5624,1,2,73,1,9),_EtsysNacApplAuthenticationDroppedPackets_Type())
etsysNacApplAuthenticationDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplAuthenticationDroppedPackets.setStatus(_A)
_EtsysNacApplAuthenticationUnknownTypes_Type=Counter64
_EtsysNacApplAuthenticationUnknownTypes_Object=MibScalar
etsysNacApplAuthenticationUnknownTypes=_EtsysNacApplAuthenticationUnknownTypes_Object((1,3,6,1,4,1,5624,1,2,73,1,10),_EtsysNacApplAuthenticationUnknownTypes_Type())
etsysNacApplAuthenticationUnknownTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplAuthenticationUnknownTypes.setStatus(_A)
_EtsysNacApplAssessmentRequests_Type=Counter64
_EtsysNacApplAssessmentRequests_Object=MibScalar
etsysNacApplAssessmentRequests=_EtsysNacApplAssessmentRequests_Object((1,3,6,1,4,1,5624,1,2,73,1,11),_EtsysNacApplAssessmentRequests_Type())
etsysNacApplAssessmentRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplAssessmentRequests.setStatus(_A)
_EtsysNacApplCaptivePortalRequests_Type=Counter64
_EtsysNacApplCaptivePortalRequests_Object=MibScalar
etsysNacApplCaptivePortalRequests=_EtsysNacApplCaptivePortalRequests_Object((1,3,6,1,4,1,5624,1,2,73,1,12),_EtsysNacApplCaptivePortalRequests_Type())
etsysNacApplCaptivePortalRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplCaptivePortalRequests.setStatus(_A)
_EtsysNacApplContactLostSwitches_Type=Counter64
_EtsysNacApplContactLostSwitches_Object=MibScalar
etsysNacApplContactLostSwitches=_EtsysNacApplContactLostSwitches_Object((1,3,6,1,4,1,5624,1,2,73,1,13),_EtsysNacApplContactLostSwitches_Type())
etsysNacApplContactLostSwitches.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplContactLostSwitches.setStatus(_A)
_EtsysNacApplIPResolutionFailures_Type=Counter64
_EtsysNacApplIPResolutionFailures_Object=MibScalar
etsysNacApplIPResolutionFailures=_EtsysNacApplIPResolutionFailures_Object((1,3,6,1,4,1,5624,1,2,73,1,14),_EtsysNacApplIPResolutionFailures_Type())
etsysNacApplIPResolutionFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplIPResolutionFailures.setStatus(_A)
_EtsysNacApplIPResolutionTimeouts_Type=Counter64
_EtsysNacApplIPResolutionTimeouts_Object=MibScalar
etsysNacApplIPResolutionTimeouts=_EtsysNacApplIPResolutionTimeouts_Object((1,3,6,1,4,1,5624,1,2,73,1,15),_EtsysNacApplIPResolutionTimeouts_Type())
etsysNacApplIPResolutionTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplIPResolutionTimeouts.setStatus(_A)
_EtsysNacApplConnectedAgents_Type=Counter64
_EtsysNacApplConnectedAgents_Object=MibScalar
etsysNacApplConnectedAgents=_EtsysNacApplConnectedAgents_Object((1,3,6,1,4,1,5624,1,2,73,1,16),_EtsysNacApplConnectedAgents_Type())
etsysNacApplConnectedAgents.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysNacApplConnectedAgents.setStatus(_A)
_EtsysNacApplianceMIBConformance_ObjectIdentity=ObjectIdentity
etsysNacApplianceMIBConformance=_EtsysNacApplianceMIBConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,73,2))
_EtsysNacApplianceMIBGroups_ObjectIdentity=ObjectIdentity
etsysNacApplianceMIBGroups=_EtsysNacApplianceMIBGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,73,2,1))
_EtsysNacApplianceMIBCompliances_ObjectIdentity=ObjectIdentity
etsysNacApplianceMIBCompliances=_EtsysNacApplianceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,73,2,2))
etsysNacApplianceMIBGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,73,2,1,1))
etsysNacApplianceMIBGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:etsysNacApplianceMIBGroup.setStatus(_A)
etsysNacApplianceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,73,2,2,1))
etsysNacApplianceMIBCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:etsysNacApplianceMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysNacApplianceMIB':etsysNacApplianceMIB,'etsysNacApplianceObjects':etsysNacApplianceObjects,_D:etsysNacApplAuthenticationRequests,_E:etsysNacApplAuthenticationSuccesses,_F:etsysNacApplAuthenticationFailures,_G:etsysNacApplRadiusChallenges,_H:etsysNacApplAuthenticationInvalidRequests,_I:etsysNacApplAuthenticationDuplicateRequests,_J:etsysNacApplAuthenticationMalformedRequests,_K:etsysNacApplAuthenticationBadRequests,_L:etsysNacApplAuthenticationDroppedPackets,_M:etsysNacApplAuthenticationUnknownTypes,_N:etsysNacApplAssessmentRequests,_O:etsysNacApplCaptivePortalRequests,_P:etsysNacApplContactLostSwitches,_Q:etsysNacApplIPResolutionFailures,_R:etsysNacApplIPResolutionTimeouts,_S:etsysNacApplConnectedAgents,'etsysNacApplianceMIBConformance':etsysNacApplianceMIBConformance,'etsysNacApplianceMIBGroups':etsysNacApplianceMIBGroups,_T:etsysNacApplianceMIBGroup,'etsysNacApplianceMIBCompliances':etsysNacApplianceMIBCompliances,'etsysNacApplianceMIBCompliance':etsysNacApplianceMIBCompliance})