_X='clemNotificationControlGroup'
_W='clemNotificationGroup'
_V='clemIfCounterGroup'
_U='clemThresholdGroup'
_T='clemGlobalGroup'
_S='clemHighThresholdExceeded'
_R='clemLowThresholdExceeded'
_Q='clemNotifEnable'
_P='clemIfCounterEnable'
_O='clemAction'
_N='clemSamplingTimes'
_M='clemSamplingInterval'
_L='clemEnabled'
_K='clemIfCounterType'
_J='not-accessible'
_I='clemThresholdCounterType'
_H='Integer32'
_G='clemThresholdHigh'
_F='clemThresholdLow'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='CISCO-LINK-ERROR-MONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoLinkErrorMonitorMIB=ModuleIdentity((1,3,6,1,4,1,9,9,426))
if mibBuilder.loadTexts:ciscoLinkErrorMonitorMIB.setRevisions(('2004-11-19 00:00',))
class ClemCounterType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rxcrc',1),('txcrc',2),('inerrors',3)))
_CiscoLinkErrMonMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLinkErrMonMIBNotifs=_CiscoLinkErrMonMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,426,0))
_CiscoLinkErrMonMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLinkErrMonMIBObjects=_CiscoLinkErrMonMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,426,1))
_ClemGlobalObjects_ObjectIdentity=ObjectIdentity
clemGlobalObjects=_ClemGlobalObjects_ObjectIdentity((1,3,6,1,4,1,9,9,426,1,1))
_ClemEnabled_Type=TruthValue
_ClemEnabled_Object=MibScalar
clemEnabled=_ClemEnabled_Object((1,3,6,1,4,1,9,9,426,1,1,1),_ClemEnabled_Type())
clemEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:clemEnabled.setStatus(_A)
_ClemSamplingInterval_Type=Unsigned32
_ClemSamplingInterval_Object=MibScalar
clemSamplingInterval=_ClemSamplingInterval_Object((1,3,6,1,4,1,9,9,426,1,1,2),_ClemSamplingInterval_Type())
clemSamplingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:clemSamplingInterval.setStatus(_A)
if mibBuilder.loadTexts:clemSamplingInterval.setUnits('seconds')
_ClemSamplingTimes_Type=Unsigned32
_ClemSamplingTimes_Object=MibScalar
clemSamplingTimes=_ClemSamplingTimes_Object((1,3,6,1,4,1,9,9,426,1,1,3),_ClemSamplingTimes_Type())
clemSamplingTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:clemSamplingTimes.setStatus(_A)
class _ClemAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('errdisable',1),('failover',2)))
_ClemAction_Type.__name__=_H
_ClemAction_Object=MibScalar
clemAction=_ClemAction_Object((1,3,6,1,4,1,9,9,426,1,1,4),_ClemAction_Type())
clemAction.setMaxAccess(_C)
if mibBuilder.loadTexts:clemAction.setStatus(_A)
_ClemThresholdTable_Object=MibTable
clemThresholdTable=_ClemThresholdTable_Object((1,3,6,1,4,1,9,9,426,1,1,5))
if mibBuilder.loadTexts:clemThresholdTable.setStatus(_A)
_ClemThresholdEntry_Object=MibTableRow
clemThresholdEntry=_ClemThresholdEntry_Object((1,3,6,1,4,1,9,9,426,1,1,5,1))
clemThresholdEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:clemThresholdEntry.setStatus(_A)
_ClemThresholdCounterType_Type=ClemCounterType
_ClemThresholdCounterType_Object=MibTableColumn
clemThresholdCounterType=_ClemThresholdCounterType_Object((1,3,6,1,4,1,9,9,426,1,1,5,1,1),_ClemThresholdCounterType_Type())
clemThresholdCounterType.setMaxAccess(_J)
if mibBuilder.loadTexts:clemThresholdCounterType.setStatus(_A)
_ClemThresholdLow_Type=Unsigned32
_ClemThresholdLow_Object=MibTableColumn
clemThresholdLow=_ClemThresholdLow_Object((1,3,6,1,4,1,9,9,426,1,1,5,1,2),_ClemThresholdLow_Type())
clemThresholdLow.setMaxAccess(_C)
if mibBuilder.loadTexts:clemThresholdLow.setStatus(_A)
_ClemThresholdHigh_Type=Unsigned32
_ClemThresholdHigh_Object=MibTableColumn
clemThresholdHigh=_ClemThresholdHigh_Object((1,3,6,1,4,1,9,9,426,1,1,5,1,3),_ClemThresholdHigh_Type())
clemThresholdHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:clemThresholdHigh.setStatus(_A)
class _ClemNotifEnable_Type(Bits):namedValues=NamedValues(*(('lowThresholdExceeded',0),('highThresholdExceeded',1)))
_ClemNotifEnable_Type.__name__='Bits'
_ClemNotifEnable_Object=MibScalar
clemNotifEnable=_ClemNotifEnable_Object((1,3,6,1,4,1,9,9,426,1,1,6),_ClemNotifEnable_Type())
clemNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:clemNotifEnable.setStatus(_A)
_ClemInterfaceObjects_ObjectIdentity=ObjectIdentity
clemInterfaceObjects=_ClemInterfaceObjects_ObjectIdentity((1,3,6,1,4,1,9,9,426,1,2))
_ClemIfCounterTable_Object=MibTable
clemIfCounterTable=_ClemIfCounterTable_Object((1,3,6,1,4,1,9,9,426,1,2,1))
if mibBuilder.loadTexts:clemIfCounterTable.setStatus(_A)
_ClemIfCounterEntry_Object=MibTableRow
clemIfCounterEntry=_ClemIfCounterEntry_Object((1,3,6,1,4,1,9,9,426,1,2,1,1))
clemIfCounterEntry.setIndexNames((0,_D,_E),(0,_B,_K))
if mibBuilder.loadTexts:clemIfCounterEntry.setStatus(_A)
_ClemIfCounterType_Type=ClemCounterType
_ClemIfCounterType_Object=MibTableColumn
clemIfCounterType=_ClemIfCounterType_Object((1,3,6,1,4,1,9,9,426,1,2,1,1,1),_ClemIfCounterType_Type())
clemIfCounterType.setMaxAccess(_J)
if mibBuilder.loadTexts:clemIfCounterType.setStatus(_A)
_ClemIfCounterEnable_Type=TruthValue
_ClemIfCounterEnable_Object=MibTableColumn
clemIfCounterEnable=_ClemIfCounterEnable_Object((1,3,6,1,4,1,9,9,426,1,2,1,1,2),_ClemIfCounterEnable_Type())
clemIfCounterEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:clemIfCounterEnable.setStatus(_A)
_CiscoLinkErrMonMIBConform_ObjectIdentity=ObjectIdentity
ciscoLinkErrMonMIBConform=_CiscoLinkErrMonMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,426,2))
_CiscoLinkErrMonMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLinkErrMonMIBCompliances=_CiscoLinkErrMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,426,2,1))
_CiscoLinkErrMonMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLinkErrMonMIBGroups=_CiscoLinkErrMonMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,426,2,2))
clemGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,426,2,2,1))
clemGlobalGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:clemGlobalGroup.setStatus(_A)
clemThresholdGroup=ObjectGroup((1,3,6,1,4,1,9,9,426,2,2,2))
clemThresholdGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:clemThresholdGroup.setStatus(_A)
clemIfCounterGroup=ObjectGroup((1,3,6,1,4,1,9,9,426,2,2,3))
clemIfCounterGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:clemIfCounterGroup.setStatus(_A)
clemNotificationControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,426,2,2,5))
clemNotificationControlGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:clemNotificationControlGroup.setStatus(_A)
clemLowThresholdExceeded=NotificationType((1,3,6,1,4,1,9,9,426,0,1))
clemLowThresholdExceeded.setObjects(*((_B,_F),(_D,_E)))
if mibBuilder.loadTexts:clemLowThresholdExceeded.setStatus(_A)
clemHighThresholdExceeded=NotificationType((1,3,6,1,4,1,9,9,426,0,2))
clemHighThresholdExceeded.setObjects(*((_B,_G),(_D,_E)))
if mibBuilder.loadTexts:clemHighThresholdExceeded.setStatus(_A)
clemNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,426,2,2,4))
clemNotificationGroup.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:clemNotificationGroup.setStatus(_A)
ciscoLinkErrMonMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,426,2,1,1))
ciscoLinkErrMonMIBCompliance.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoLinkErrMonMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ClemCounterType':ClemCounterType,'ciscoLinkErrorMonitorMIB':ciscoLinkErrorMonitorMIB,'ciscoLinkErrMonMIBNotifs':ciscoLinkErrMonMIBNotifs,_R:clemLowThresholdExceeded,_S:clemHighThresholdExceeded,'ciscoLinkErrMonMIBObjects':ciscoLinkErrMonMIBObjects,'clemGlobalObjects':clemGlobalObjects,_L:clemEnabled,_M:clemSamplingInterval,_N:clemSamplingTimes,_O:clemAction,'clemThresholdTable':clemThresholdTable,'clemThresholdEntry':clemThresholdEntry,_I:clemThresholdCounterType,_F:clemThresholdLow,_G:clemThresholdHigh,_Q:clemNotifEnable,'clemInterfaceObjects':clemInterfaceObjects,'clemIfCounterTable':clemIfCounterTable,'clemIfCounterEntry':clemIfCounterEntry,_K:clemIfCounterType,_P:clemIfCounterEnable,'ciscoLinkErrMonMIBConform':ciscoLinkErrMonMIBConform,'ciscoLinkErrMonMIBCompliances':ciscoLinkErrMonMIBCompliances,'ciscoLinkErrMonMIBCompliance':ciscoLinkErrMonMIBCompliance,'ciscoLinkErrMonMIBGroups':ciscoLinkErrMonMIBGroups,_T:clemGlobalGroup,_U:clemThresholdGroup,_V:clemIfCounterGroup,_W:clemNotificationGroup,_X:clemNotificationControlGroup})