_S='hmIOModValueDigOutputValue'
_R='hmIOModValueDigInputValue'
_Q='hmIOModValueDigOutputID'
_P='hmIOModValueDigOutputModID'
_O='read-only'
_N='not-available'
_M='hmIOModValueDigInputID'
_L='hmIOModValueDigInputModID'
_K='hmIOModConfigDigOutputID'
_J='hmIOModConfigDigOutputModID'
_I='hmIOModConfigDigInputID'
_H='hmIOModConfigDigInputModID'
_G='InetPortNumber'
_F='HmEnabledStatus'
_E='not-accessible'
_D='HMIOMODULE-SNMP-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmChassis,hmChassisEvent=mibBuilder.importSymbols('HMPRIV-MGMT-SNMP-MIB','hmChassis','hmChassisEvent')
InetPortNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hmIOModuleGroup=ModuleIdentity((1,3,6,1,4,1,248,14,1,13))
if mibBuilder.loadTexts:hmIOModuleGroup.setRevisions(('2010-11-08 15:00',))
class HmEnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HmIOModuleConfigGroup_ObjectIdentity=ObjectIdentity
hmIOModuleConfigGroup=_HmIOModuleConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,14,1,13,1))
_HmIOModConfigCommon_ObjectIdentity=ObjectIdentity
hmIOModConfigCommon=_HmIOModConfigCommon_ObjectIdentity((1,3,6,1,4,1,248,14,1,13,1,1))
class _HmIOModConfigDigInputAdminState_Type(HmEnabledStatus):defaultValue=2
_HmIOModConfigDigInputAdminState_Type.__name__=_F
_HmIOModConfigDigInputAdminState_Object=MibScalar
hmIOModConfigDigInputAdminState=_HmIOModConfigDigInputAdminState_Object((1,3,6,1,4,1,248,14,1,13,1,1,1),_HmIOModConfigDigInputAdminState_Type())
hmIOModConfigDigInputAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigInputAdminState.setStatus(_A)
class _HmIOModConfigDigOutputAdminState_Type(HmEnabledStatus):defaultValue=2
_HmIOModConfigDigOutputAdminState_Type.__name__=_F
_HmIOModConfigDigOutputAdminState_Object=MibScalar
hmIOModConfigDigOutputAdminState=_HmIOModConfigDigOutputAdminState_Object((1,3,6,1,4,1,248,14,1,13,1,1,2),_HmIOModConfigDigOutputAdminState_Type())
hmIOModConfigDigOutputAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigOutputAdminState.setStatus(_A)
class _HmIOModConfigDigInputRefreshInterval_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,10000))
_HmIOModConfigDigInputRefreshInterval_Type.__name__=_B
_HmIOModConfigDigInputRefreshInterval_Object=MibScalar
hmIOModConfigDigInputRefreshInterval=_HmIOModConfigDigInputRefreshInterval_Object((1,3,6,1,4,1,248,14,1,13,1,1,3),_HmIOModConfigDigInputRefreshInterval_Type())
hmIOModConfigDigInputRefreshInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigInputRefreshInterval.setStatus(_A)
class _HmIOModConfigDigOutputRefreshInterval_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,10000))
_HmIOModConfigDigOutputRefreshInterval_Type.__name__=_B
_HmIOModConfigDigOutputRefreshInterval_Object=MibScalar
hmIOModConfigDigOutputRefreshInterval=_HmIOModConfigDigOutputRefreshInterval_Object((1,3,6,1,4,1,248,14,1,13,1,1,4),_HmIOModConfigDigOutputRefreshInterval_Type())
hmIOModConfigDigOutputRefreshInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigOutputRefreshInterval.setStatus(_A)
class _HmIOModConfigDigOutputRetryCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HmIOModConfigDigOutputRetryCount_Type.__name__=_B
_HmIOModConfigDigOutputRetryCount_Object=MibScalar
hmIOModConfigDigOutputRetryCount=_HmIOModConfigDigOutputRetryCount_Object((1,3,6,1,4,1,248,14,1,13,1,1,5),_HmIOModConfigDigOutputRetryCount_Type())
hmIOModConfigDigOutputRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigOutputRetryCount.setStatus(_A)
_HmIOModConfigDigInputTable_Object=MibTable
hmIOModConfigDigInputTable=_HmIOModConfigDigInputTable_Object((1,3,6,1,4,1,248,14,1,13,1,2))
if mibBuilder.loadTexts:hmIOModConfigDigInputTable.setStatus(_A)
_HmIOModConfigDigInputEntry_Object=MibTableRow
hmIOModConfigDigInputEntry=_HmIOModConfigDigInputEntry_Object((1,3,6,1,4,1,248,14,1,13,1,2,1))
hmIOModConfigDigInputEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:hmIOModConfigDigInputEntry.setStatus(_A)
class _HmIOModConfigDigInputModID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_HmIOModConfigDigInputModID_Type.__name__=_B
_HmIOModConfigDigInputModID_Object=MibTableColumn
hmIOModConfigDigInputModID=_HmIOModConfigDigInputModID_Object((1,3,6,1,4,1,248,14,1,13,1,2,1,1),_HmIOModConfigDigInputModID_Type())
hmIOModConfigDigInputModID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmIOModConfigDigInputModID.setStatus(_A)
class _HmIOModConfigDigInputID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HmIOModConfigDigInputID_Type.__name__=_B
_HmIOModConfigDigInputID_Object=MibTableColumn
hmIOModConfigDigInputID=_HmIOModConfigDigInputID_Object((1,3,6,1,4,1,248,14,1,13,1,2,1,2),_HmIOModConfigDigInputID_Type())
hmIOModConfigDigInputID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmIOModConfigDigInputID.setStatus(_A)
class _HmIOModConfigDigInputLogEvent_Type(HmEnabledStatus):defaultValue=2
_HmIOModConfigDigInputLogEvent_Type.__name__=_F
_HmIOModConfigDigInputLogEvent_Object=MibTableColumn
hmIOModConfigDigInputLogEvent=_HmIOModConfigDigInputLogEvent_Object((1,3,6,1,4,1,248,14,1,13,1,2,1,3),_HmIOModConfigDigInputLogEvent_Type())
hmIOModConfigDigInputLogEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigInputLogEvent.setStatus(_A)
class _HmIOModConfigDigInputSnmpTrap_Type(HmEnabledStatus):defaultValue=2
_HmIOModConfigDigInputSnmpTrap_Type.__name__=_F
_HmIOModConfigDigInputSnmpTrap_Object=MibTableColumn
hmIOModConfigDigInputSnmpTrap=_HmIOModConfigDigInputSnmpTrap_Object((1,3,6,1,4,1,248,14,1,13,1,2,1,4),_HmIOModConfigDigInputSnmpTrap_Type())
hmIOModConfigDigInputSnmpTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigInputSnmpTrap.setStatus(_A)
_HmIOModConfigDigOutputTable_Object=MibTable
hmIOModConfigDigOutputTable=_HmIOModConfigDigOutputTable_Object((1,3,6,1,4,1,248,14,1,13,1,3))
if mibBuilder.loadTexts:hmIOModConfigDigOutputTable.setStatus(_A)
_HmIOModConfigDigOutputEntry_Object=MibTableRow
hmIOModConfigDigOutputEntry=_HmIOModConfigDigOutputEntry_Object((1,3,6,1,4,1,248,14,1,13,1,3,1))
hmIOModConfigDigOutputEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:hmIOModConfigDigOutputEntry.setStatus(_A)
class _HmIOModConfigDigOutputModID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_HmIOModConfigDigOutputModID_Type.__name__=_B
_HmIOModConfigDigOutputModID_Object=MibTableColumn
hmIOModConfigDigOutputModID=_HmIOModConfigDigOutputModID_Object((1,3,6,1,4,1,248,14,1,13,1,3,1,1),_HmIOModConfigDigOutputModID_Type())
hmIOModConfigDigOutputModID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmIOModConfigDigOutputModID.setStatus(_A)
class _HmIOModConfigDigOutputID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HmIOModConfigDigOutputID_Type.__name__=_B
_HmIOModConfigDigOutputID_Object=MibTableColumn
hmIOModConfigDigOutputID=_HmIOModConfigDigOutputID_Object((1,3,6,1,4,1,248,14,1,13,1,3,1,2),_HmIOModConfigDigOutputID_Type())
hmIOModConfigDigOutputID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmIOModConfigDigOutputID.setStatus(_A)
class _HmIOModConfigDigOutputLogEvent_Type(HmEnabledStatus):defaultValue=2
_HmIOModConfigDigOutputLogEvent_Type.__name__=_F
_HmIOModConfigDigOutputLogEvent_Object=MibTableColumn
hmIOModConfigDigOutputLogEvent=_HmIOModConfigDigOutputLogEvent_Object((1,3,6,1,4,1,248,14,1,13,1,3,1,3),_HmIOModConfigDigOutputLogEvent_Type())
hmIOModConfigDigOutputLogEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigOutputLogEvent.setStatus(_A)
class _HmIOModConfigDigOutputSnmpTrap_Type(HmEnabledStatus):defaultValue=2
_HmIOModConfigDigOutputSnmpTrap_Type.__name__=_F
_HmIOModConfigDigOutputSnmpTrap_Object=MibTableColumn
hmIOModConfigDigOutputSnmpTrap=_HmIOModConfigDigOutputSnmpTrap_Object((1,3,6,1,4,1,248,14,1,13,1,3,1,4),_HmIOModConfigDigOutputSnmpTrap_Type())
hmIOModConfigDigOutputSnmpTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigOutputSnmpTrap.setStatus(_A)
_HmIOModConfigDigOutputSourceIP_Type=IpAddress
_HmIOModConfigDigOutputSourceIP_Object=MibTableColumn
hmIOModConfigDigOutputSourceIP=_HmIOModConfigDigOutputSourceIP_Object((1,3,6,1,4,1,248,14,1,13,1,3,1,5),_HmIOModConfigDigOutputSourceIP_Type())
hmIOModConfigDigOutputSourceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigOutputSourceIP.setStatus(_A)
class _HmIOModConfigDigOutputSourceModID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_HmIOModConfigDigOutputSourceModID_Type.__name__=_B
_HmIOModConfigDigOutputSourceModID_Object=MibTableColumn
hmIOModConfigDigOutputSourceModID=_HmIOModConfigDigOutputSourceModID_Object((1,3,6,1,4,1,248,14,1,13,1,3,1,6),_HmIOModConfigDigOutputSourceModID_Type())
hmIOModConfigDigOutputSourceModID.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigOutputSourceModID.setStatus(_A)
class _HmIOModConfigDigOutputSourceID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HmIOModConfigDigOutputSourceID_Type.__name__=_B
_HmIOModConfigDigOutputSourceID_Object=MibTableColumn
hmIOModConfigDigOutputSourceID=_HmIOModConfigDigOutputSourceID_Object((1,3,6,1,4,1,248,14,1,13,1,3,1,7),_HmIOModConfigDigOutputSourceID_Type())
hmIOModConfigDigOutputSourceID.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigOutputSourceID.setStatus(_A)
class _HmIOModConfigDigOutputSourcePort_Type(InetPortNumber):defaultValue=161
_HmIOModConfigDigOutputSourcePort_Type.__name__=_G
_HmIOModConfigDigOutputSourcePort_Object=MibTableColumn
hmIOModConfigDigOutputSourcePort=_HmIOModConfigDigOutputSourcePort_Object((1,3,6,1,4,1,248,14,1,13,1,3,1,8),_HmIOModConfigDigOutputSourcePort_Type())
hmIOModConfigDigOutputSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:hmIOModConfigDigOutputSourcePort.setStatus(_A)
_HmIOModuleValueGroup_ObjectIdentity=ObjectIdentity
hmIOModuleValueGroup=_HmIOModuleValueGroup_ObjectIdentity((1,3,6,1,4,1,248,14,1,13,2))
_HmIOModValueDigInputTable_Object=MibTable
hmIOModValueDigInputTable=_HmIOModValueDigInputTable_Object((1,3,6,1,4,1,248,14,1,13,2,1))
if mibBuilder.loadTexts:hmIOModValueDigInputTable.setStatus(_A)
_HmIOModValueDigInputEntry_Object=MibTableRow
hmIOModValueDigInputEntry=_HmIOModValueDigInputEntry_Object((1,3,6,1,4,1,248,14,1,13,2,1,1))
hmIOModValueDigInputEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:hmIOModValueDigInputEntry.setStatus(_A)
class _HmIOModValueDigInputModID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_HmIOModValueDigInputModID_Type.__name__=_B
_HmIOModValueDigInputModID_Object=MibTableColumn
hmIOModValueDigInputModID=_HmIOModValueDigInputModID_Object((1,3,6,1,4,1,248,14,1,13,2,1,1,1),_HmIOModValueDigInputModID_Type())
hmIOModValueDigInputModID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmIOModValueDigInputModID.setStatus(_A)
class _HmIOModValueDigInputID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HmIOModValueDigInputID_Type.__name__=_B
_HmIOModValueDigInputID_Object=MibTableColumn
hmIOModValueDigInputID=_HmIOModValueDigInputID_Object((1,3,6,1,4,1,248,14,1,13,2,1,1,2),_HmIOModValueDigInputID_Type())
hmIOModValueDigInputID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmIOModValueDigInputID.setStatus(_A)
class _HmIOModValueDigInputValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('high',1),('low',2)))
_HmIOModValueDigInputValue_Type.__name__=_B
_HmIOModValueDigInputValue_Object=MibTableColumn
hmIOModValueDigInputValue=_HmIOModValueDigInputValue_Object((1,3,6,1,4,1,248,14,1,13,2,1,1,3),_HmIOModValueDigInputValue_Type())
hmIOModValueDigInputValue.setMaxAccess(_O)
if mibBuilder.loadTexts:hmIOModValueDigInputValue.setStatus(_A)
_HmIOModValueDigOutputTable_Object=MibTable
hmIOModValueDigOutputTable=_HmIOModValueDigOutputTable_Object((1,3,6,1,4,1,248,14,1,13,2,2))
if mibBuilder.loadTexts:hmIOModValueDigOutputTable.setStatus(_A)
_HmIOModValueDigOutputEntry_Object=MibTableRow
hmIOModValueDigOutputEntry=_HmIOModValueDigOutputEntry_Object((1,3,6,1,4,1,248,14,1,13,2,2,1))
hmIOModValueDigOutputEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:hmIOModValueDigOutputEntry.setStatus(_A)
class _HmIOModValueDigOutputModID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_HmIOModValueDigOutputModID_Type.__name__=_B
_HmIOModValueDigOutputModID_Object=MibTableColumn
hmIOModValueDigOutputModID=_HmIOModValueDigOutputModID_Object((1,3,6,1,4,1,248,14,1,13,2,2,1,1),_HmIOModValueDigOutputModID_Type())
hmIOModValueDigOutputModID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmIOModValueDigOutputModID.setStatus(_A)
class _HmIOModValueDigOutputID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HmIOModValueDigOutputID_Type.__name__=_B
_HmIOModValueDigOutputID_Object=MibTableColumn
hmIOModValueDigOutputID=_HmIOModValueDigOutputID_Object((1,3,6,1,4,1,248,14,1,13,2,2,1,2),_HmIOModValueDigOutputID_Type())
hmIOModValueDigOutputID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmIOModValueDigOutputID.setStatus(_A)
class _HmIOModValueDigOutputValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_N,0),('high',1),('low',2),('invalid',3),('not-configured',4)))
_HmIOModValueDigOutputValue_Type.__name__=_B
_HmIOModValueDigOutputValue_Object=MibTableColumn
hmIOModValueDigOutputValue=_HmIOModValueDigOutputValue_Object((1,3,6,1,4,1,248,14,1,13,2,2,1,3),_HmIOModValueDigOutputValue_Type())
hmIOModValueDigOutputValue.setMaxAccess(_O)
if mibBuilder.loadTexts:hmIOModValueDigOutputValue.setStatus(_A)
hmIOModDigInputChangeTrap=NotificationType((1,3,6,1,4,1,248,14,1,0,16))
hmIOModDigInputChangeTrap.setObjects((_D,_R))
if mibBuilder.loadTexts:hmIOModDigInputChangeTrap.setStatus(_A)
hmIOModDigOutputChangeTrap=NotificationType((1,3,6,1,4,1,248,14,1,0,17))
hmIOModDigOutputChangeTrap.setObjects((_D,_S))
if mibBuilder.loadTexts:hmIOModDigOutputChangeTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_F:HmEnabledStatus,'hmIOModDigInputChangeTrap':hmIOModDigInputChangeTrap,'hmIOModDigOutputChangeTrap':hmIOModDigOutputChangeTrap,'hmIOModuleGroup':hmIOModuleGroup,'hmIOModuleConfigGroup':hmIOModuleConfigGroup,'hmIOModConfigCommon':hmIOModConfigCommon,'hmIOModConfigDigInputAdminState':hmIOModConfigDigInputAdminState,'hmIOModConfigDigOutputAdminState':hmIOModConfigDigOutputAdminState,'hmIOModConfigDigInputRefreshInterval':hmIOModConfigDigInputRefreshInterval,'hmIOModConfigDigOutputRefreshInterval':hmIOModConfigDigOutputRefreshInterval,'hmIOModConfigDigOutputRetryCount':hmIOModConfigDigOutputRetryCount,'hmIOModConfigDigInputTable':hmIOModConfigDigInputTable,'hmIOModConfigDigInputEntry':hmIOModConfigDigInputEntry,_H:hmIOModConfigDigInputModID,_I:hmIOModConfigDigInputID,'hmIOModConfigDigInputLogEvent':hmIOModConfigDigInputLogEvent,'hmIOModConfigDigInputSnmpTrap':hmIOModConfigDigInputSnmpTrap,'hmIOModConfigDigOutputTable':hmIOModConfigDigOutputTable,'hmIOModConfigDigOutputEntry':hmIOModConfigDigOutputEntry,_J:hmIOModConfigDigOutputModID,_K:hmIOModConfigDigOutputID,'hmIOModConfigDigOutputLogEvent':hmIOModConfigDigOutputLogEvent,'hmIOModConfigDigOutputSnmpTrap':hmIOModConfigDigOutputSnmpTrap,'hmIOModConfigDigOutputSourceIP':hmIOModConfigDigOutputSourceIP,'hmIOModConfigDigOutputSourceModID':hmIOModConfigDigOutputSourceModID,'hmIOModConfigDigOutputSourceID':hmIOModConfigDigOutputSourceID,'hmIOModConfigDigOutputSourcePort':hmIOModConfigDigOutputSourcePort,'hmIOModuleValueGroup':hmIOModuleValueGroup,'hmIOModValueDigInputTable':hmIOModValueDigInputTable,'hmIOModValueDigInputEntry':hmIOModValueDigInputEntry,_L:hmIOModValueDigInputModID,_M:hmIOModValueDigInputID,_R:hmIOModValueDigInputValue,'hmIOModValueDigOutputTable':hmIOModValueDigOutputTable,'hmIOModValueDigOutputEntry':hmIOModValueDigOutputEntry,_P:hmIOModValueDigOutputModID,_Q:hmIOModValueDigOutputID,_S:hmIOModValueDigOutputValue})