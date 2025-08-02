_G='adGenAOSOverTempProtectionNotificationGroup'
_F='adGenAOSOverTempProtectionShutdownResume'
_E='adGenAOSOverTempProtectionWarningResume'
_D='adGenAOSOverTempProtectionShutdown'
_C='adGenAOSOverTempProtectionWarning'
_B='ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSCommon,adGenAOSConformance=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSCommon','adGenAOSConformance')
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAOSOverTempProtectionMib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,1,10))
if mibBuilder.loadTexts:adGenAOSOverTempProtectionMib.setRevisions(('2017-12-27 00:00','2014-11-04 16:15'))
_AdGenAOSOverTempProtection_ObjectIdentity=ObjectIdentity
adGenAOSOverTempProtection=_AdGenAOSOverTempProtection_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,10))
_AdGenAOSOverTempProtectionTrap_ObjectIdentity=ObjectIdentity
adGenAOSOverTempProtectionTrap=_AdGenAOSOverTempProtectionTrap_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,10,0))
_AdGenAOSOverTempProtectionConformance_ObjectIdentity=ObjectIdentity
adGenAOSOverTempProtectionConformance=_AdGenAOSOverTempProtectionConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,19))
_AdGenAOSOverTempProtectionGroups_ObjectIdentity=ObjectIdentity
adGenAOSOverTempProtectionGroups=_AdGenAOSOverTempProtectionGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,19,1))
_AdGenAOSOverTempProtectionCompliances_ObjectIdentity=ObjectIdentity
adGenAOSOverTempProtectionCompliances=_AdGenAOSOverTempProtectionCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,19,2))
adGenAOSOverTempProtectionWarning=NotificationType((1,3,6,1,4,1,664,5,53,1,10,0,1))
if mibBuilder.loadTexts:adGenAOSOverTempProtectionWarning.setStatus(_A)
adGenAOSOverTempProtectionShutdown=NotificationType((1,3,6,1,4,1,664,5,53,1,10,0,2))
if mibBuilder.loadTexts:adGenAOSOverTempProtectionShutdown.setStatus(_A)
adGenAOSOverTempProtectionWarningResume=NotificationType((1,3,6,1,4,1,664,5,53,1,10,0,3))
if mibBuilder.loadTexts:adGenAOSOverTempProtectionWarningResume.setStatus(_A)
adGenAOSOverTempProtectionShutdownResume=NotificationType((1,3,6,1,4,1,664,5,53,1,10,0,4))
if mibBuilder.loadTexts:adGenAOSOverTempProtectionShutdownResume.setStatus(_A)
adGenAOSOverTempProtectionNotificationGroup=NotificationGroup((1,3,6,1,4,1,664,5,53,99,19,1,1))
adGenAOSOverTempProtectionNotificationGroup.setObjects(*((_B,_C),(_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:adGenAOSOverTempProtectionNotificationGroup.setStatus(_A)
adGenAOSOverTempProtectionFullCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,19,2,1))
adGenAOSOverTempProtectionFullCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:adGenAOSOverTempProtectionFullCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenAOSOverTempProtection':adGenAOSOverTempProtection,'adGenAOSOverTempProtectionTrap':adGenAOSOverTempProtectionTrap,_C:adGenAOSOverTempProtectionWarning,_D:adGenAOSOverTempProtectionShutdown,_E:adGenAOSOverTempProtectionWarningResume,_F:adGenAOSOverTempProtectionShutdownResume,'adGenAOSOverTempProtectionConformance':adGenAOSOverTempProtectionConformance,'adGenAOSOverTempProtectionGroups':adGenAOSOverTempProtectionGroups,_G:adGenAOSOverTempProtectionNotificationGroup,'adGenAOSOverTempProtectionCompliances':adGenAOSOverTempProtectionCompliances,'adGenAOSOverTempProtectionFullCompliance':adGenAOSOverTempProtectionFullCompliance,'adGenAOSOverTempProtectionMib':adGenAOSOverTempProtectionMib})