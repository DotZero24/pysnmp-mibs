_P='sCgmpGroup'
_O='sCgmpRouterEntryStatus'
_N='sCgmpRouterHoldTime'
_M='sCgmpFastLeaveEnable'
_L='sCgmpEnable'
_K='not-accessible'
_J='sCgmpRouterMacAddress'
_I='sCgmpRouterVlanIndex'
_H='disabled'
_G='enabled'
_F='dot1dBasePort'
_E='BRIDGE-MIB'
_D='read-write'
_C='Integer32'
_B='CISCO-SWITCH-CGMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_E,_F)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
ciscoSwitchCgmpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,101))
if mibBuilder.loadTexts:ciscoSwitchCgmpMIB.setRevisions(('1998-05-07 00:00',))
class SCgmpVlanIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_CiscoSwitchCgmpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSwitchCgmpMIBObjects=_CiscoSwitchCgmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,101,1))
_SCgmpInfo_ObjectIdentity=ObjectIdentity
sCgmpInfo=_SCgmpInfo_ObjectIdentity((1,3,6,1,4,1,9,9,101,1,1))
class _SCgmpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SCgmpEnable_Type.__name__=_C
_SCgmpEnable_Object=MibScalar
sCgmpEnable=_SCgmpEnable_Object((1,3,6,1,4,1,9,9,101,1,1,1),_SCgmpEnable_Type())
sCgmpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sCgmpEnable.setStatus(_A)
class _SCgmpFastLeaveEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SCgmpFastLeaveEnable_Type.__name__=_C
_SCgmpFastLeaveEnable_Object=MibScalar
sCgmpFastLeaveEnable=_SCgmpFastLeaveEnable_Object((1,3,6,1,4,1,9,9,101,1,1,2),_SCgmpFastLeaveEnable_Type())
sCgmpFastLeaveEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sCgmpFastLeaveEnable.setStatus(_A)
class _SCgmpRouterHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,6000))
_SCgmpRouterHoldTime_Type.__name__=_C
_SCgmpRouterHoldTime_Object=MibScalar
sCgmpRouterHoldTime=_SCgmpRouterHoldTime_Object((1,3,6,1,4,1,9,9,101,1,1,3),_SCgmpRouterHoldTime_Type())
sCgmpRouterHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:sCgmpRouterHoldTime.setStatus(_A)
if mibBuilder.loadTexts:sCgmpRouterHoldTime.setUnits('seconds')
_SCgmpRouterTable_Object=MibTable
sCgmpRouterTable=_SCgmpRouterTable_Object((1,3,6,1,4,1,9,9,101,1,1,4))
if mibBuilder.loadTexts:sCgmpRouterTable.setStatus(_A)
_SCgmpRouterEntry_Object=MibTableRow
sCgmpRouterEntry=_SCgmpRouterEntry_Object((1,3,6,1,4,1,9,9,101,1,1,4,1))
sCgmpRouterEntry.setIndexNames((0,_B,_I),(0,_E,_F),(0,_B,_J))
if mibBuilder.loadTexts:sCgmpRouterEntry.setStatus(_A)
_SCgmpRouterVlanIndex_Type=SCgmpVlanIndex
_SCgmpRouterVlanIndex_Object=MibTableColumn
sCgmpRouterVlanIndex=_SCgmpRouterVlanIndex_Object((1,3,6,1,4,1,9,9,101,1,1,4,1,1),_SCgmpRouterVlanIndex_Type())
sCgmpRouterVlanIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:sCgmpRouterVlanIndex.setStatus(_A)
_SCgmpRouterMacAddress_Type=MacAddress
_SCgmpRouterMacAddress_Object=MibTableColumn
sCgmpRouterMacAddress=_SCgmpRouterMacAddress_Object((1,3,6,1,4,1,9,9,101,1,1,4,1,3),_SCgmpRouterMacAddress_Type())
sCgmpRouterMacAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:sCgmpRouterMacAddress.setStatus(_A)
_SCgmpRouterEntryStatus_Type=RowStatus
_SCgmpRouterEntryStatus_Object=MibTableColumn
sCgmpRouterEntryStatus=_SCgmpRouterEntryStatus_Object((1,3,6,1,4,1,9,9,101,1,1,4,1,4),_SCgmpRouterEntryStatus_Type())
sCgmpRouterEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sCgmpRouterEntryStatus.setStatus(_A)
_CiscoSwitchCgmpMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSwitchCgmpMIBConformance=_CiscoSwitchCgmpMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,101,3))
_CiscoSwitchCgmpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSwitchCgmpMIBCompliances=_CiscoSwitchCgmpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,101,3,1))
_CiscoSwitchCgmpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSwitchCgmpMIBGroups=_CiscoSwitchCgmpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,101,3,2))
sCgmpGroup=ObjectGroup((1,3,6,1,4,1,9,9,101,3,2,1))
sCgmpGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:sCgmpGroup.setStatus(_A)
ciscoSwitchCgmpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,101,3,1,1))
ciscoSwitchCgmpMIBCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:ciscoSwitchCgmpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SCgmpVlanIndex':SCgmpVlanIndex,'ciscoSwitchCgmpMIB':ciscoSwitchCgmpMIB,'ciscoSwitchCgmpMIBObjects':ciscoSwitchCgmpMIBObjects,'sCgmpInfo':sCgmpInfo,_L:sCgmpEnable,_M:sCgmpFastLeaveEnable,_N:sCgmpRouterHoldTime,'sCgmpRouterTable':sCgmpRouterTable,'sCgmpRouterEntry':sCgmpRouterEntry,_I:sCgmpRouterVlanIndex,_J:sCgmpRouterMacAddress,_O:sCgmpRouterEntryStatus,'ciscoSwitchCgmpMIBConformance':ciscoSwitchCgmpMIBConformance,'ciscoSwitchCgmpMIBCompliances':ciscoSwitchCgmpMIBCompliances,'ciscoSwitchCgmpMIBCompliance':ciscoSwitchCgmpMIBCompliance,'ciscoSwitchCgmpMIBGroups':ciscoSwitchCgmpMIBGroups,_P:sCgmpGroup})