_U='hm2IOModValueDigOutputValue'
_T='hm2IOModValueDigInputValue'
_S='hm2IOModValueDigOutputID'
_R='hm2IOModValueDigOutputModID'
_Q='read-only'
_P='not-available'
_O='hm2IOModValueDigInputID'
_N='hm2IOModValueDigInputModID'
_M='hm2IOModConfigDigOutputID'
_L='hm2IOModConfigDigOutputModID'
_K='hm2IOModConfigDigInputID'
_J='hm2IOModConfigDigInputModID'
_I='InetPortNumber'
_H='InetAddressType'
_G='InetAddress'
_F='HmEnabledStatus'
_E='not-accessible'
_D='HM2-IOMODULE-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_F,'hm2ConfigurationMibs')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2IOModuleMib=ModuleIdentity((1,3,6,1,4,1,248,11,100))
if mibBuilder.loadTexts:hm2IOModuleMib.setRevisions(('2012-02-10 00:00',))
_Hm2IOModuleMibNotifications_ObjectIdentity=ObjectIdentity
hm2IOModuleMibNotifications=_Hm2IOModuleMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,100,0))
_Hm2IOModuleMibObjects_ObjectIdentity=ObjectIdentity
hm2IOModuleMibObjects=_Hm2IOModuleMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,100,1))
_Hm2IOModConfigGroup_ObjectIdentity=ObjectIdentity
hm2IOModConfigGroup=_Hm2IOModConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,100,1,1))
_Hm2IOModConfigCommon_ObjectIdentity=ObjectIdentity
hm2IOModConfigCommon=_Hm2IOModConfigCommon_ObjectIdentity((1,3,6,1,4,1,248,11,100,1,1,1))
class _Hm2IOModConfigDigInputAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2IOModConfigDigInputAdminState_Type.__name__=_F
_Hm2IOModConfigDigInputAdminState_Object=MibScalar
hm2IOModConfigDigInputAdminState=_Hm2IOModConfigDigInputAdminState_Object((1,3,6,1,4,1,248,11,100,1,1,1,1),_Hm2IOModConfigDigInputAdminState_Type())
hm2IOModConfigDigInputAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigInputAdminState.setStatus(_A)
class _Hm2IOModConfigDigOutputAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2IOModConfigDigOutputAdminState_Type.__name__=_F
_Hm2IOModConfigDigOutputAdminState_Object=MibScalar
hm2IOModConfigDigOutputAdminState=_Hm2IOModConfigDigOutputAdminState_Object((1,3,6,1,4,1,248,11,100,1,1,1,2),_Hm2IOModConfigDigOutputAdminState_Type())
hm2IOModConfigDigOutputAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigOutputAdminState.setStatus(_A)
class _Hm2IOModConfigDigInputRefreshInterval_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,10000))
_Hm2IOModConfigDigInputRefreshInterval_Type.__name__=_B
_Hm2IOModConfigDigInputRefreshInterval_Object=MibScalar
hm2IOModConfigDigInputRefreshInterval=_Hm2IOModConfigDigInputRefreshInterval_Object((1,3,6,1,4,1,248,11,100,1,1,1,3),_Hm2IOModConfigDigInputRefreshInterval_Type())
hm2IOModConfigDigInputRefreshInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigInputRefreshInterval.setStatus(_A)
class _Hm2IOModConfigDigOutputRefreshInterval_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,10000))
_Hm2IOModConfigDigOutputRefreshInterval_Type.__name__=_B
_Hm2IOModConfigDigOutputRefreshInterval_Object=MibScalar
hm2IOModConfigDigOutputRefreshInterval=_Hm2IOModConfigDigOutputRefreshInterval_Object((1,3,6,1,4,1,248,11,100,1,1,1,4),_Hm2IOModConfigDigOutputRefreshInterval_Type())
hm2IOModConfigDigOutputRefreshInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigOutputRefreshInterval.setStatus(_A)
class _Hm2IOModConfigDigOutputRetryCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Hm2IOModConfigDigOutputRetryCount_Type.__name__=_B
_Hm2IOModConfigDigOutputRetryCount_Object=MibScalar
hm2IOModConfigDigOutputRetryCount=_Hm2IOModConfigDigOutputRetryCount_Object((1,3,6,1,4,1,248,11,100,1,1,1,5),_Hm2IOModConfigDigOutputRetryCount_Type())
hm2IOModConfigDigOutputRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigOutputRetryCount.setStatus(_A)
_Hm2IOModConfigDigInputTable_Object=MibTable
hm2IOModConfigDigInputTable=_Hm2IOModConfigDigInputTable_Object((1,3,6,1,4,1,248,11,100,1,1,2))
if mibBuilder.loadTexts:hm2IOModConfigDigInputTable.setStatus(_A)
_Hm2IOModConfigDigInputEntry_Object=MibTableRow
hm2IOModConfigDigInputEntry=_Hm2IOModConfigDigInputEntry_Object((1,3,6,1,4,1,248,11,100,1,1,2,1))
hm2IOModConfigDigInputEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:hm2IOModConfigDigInputEntry.setStatus(_A)
class _Hm2IOModConfigDigInputModID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2IOModConfigDigInputModID_Type.__name__=_B
_Hm2IOModConfigDigInputModID_Object=MibTableColumn
hm2IOModConfigDigInputModID=_Hm2IOModConfigDigInputModID_Object((1,3,6,1,4,1,248,11,100,1,1,2,1,1),_Hm2IOModConfigDigInputModID_Type())
hm2IOModConfigDigInputModID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2IOModConfigDigInputModID.setStatus(_A)
class _Hm2IOModConfigDigInputID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2IOModConfigDigInputID_Type.__name__=_B
_Hm2IOModConfigDigInputID_Object=MibTableColumn
hm2IOModConfigDigInputID=_Hm2IOModConfigDigInputID_Object((1,3,6,1,4,1,248,11,100,1,1,2,1,2),_Hm2IOModConfigDigInputID_Type())
hm2IOModConfigDigInputID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2IOModConfigDigInputID.setStatus(_A)
class _Hm2IOModConfigDigInputLogEvent_Type(HmEnabledStatus):defaultValue=2
_Hm2IOModConfigDigInputLogEvent_Type.__name__=_F
_Hm2IOModConfigDigInputLogEvent_Object=MibTableColumn
hm2IOModConfigDigInputLogEvent=_Hm2IOModConfigDigInputLogEvent_Object((1,3,6,1,4,1,248,11,100,1,1,2,1,3),_Hm2IOModConfigDigInputLogEvent_Type())
hm2IOModConfigDigInputLogEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigInputLogEvent.setStatus(_A)
class _Hm2IOModConfigDigInputSnmpTrap_Type(HmEnabledStatus):defaultValue=2
_Hm2IOModConfigDigInputSnmpTrap_Type.__name__=_F
_Hm2IOModConfigDigInputSnmpTrap_Object=MibTableColumn
hm2IOModConfigDigInputSnmpTrap=_Hm2IOModConfigDigInputSnmpTrap_Object((1,3,6,1,4,1,248,11,100,1,1,2,1,4),_Hm2IOModConfigDigInputSnmpTrap_Type())
hm2IOModConfigDigInputSnmpTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigInputSnmpTrap.setStatus(_A)
_Hm2IOModConfigDigOutputTable_Object=MibTable
hm2IOModConfigDigOutputTable=_Hm2IOModConfigDigOutputTable_Object((1,3,6,1,4,1,248,11,100,1,1,3))
if mibBuilder.loadTexts:hm2IOModConfigDigOutputTable.setStatus(_A)
_Hm2IOModConfigDigOutputEntry_Object=MibTableRow
hm2IOModConfigDigOutputEntry=_Hm2IOModConfigDigOutputEntry_Object((1,3,6,1,4,1,248,11,100,1,1,3,1))
hm2IOModConfigDigOutputEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:hm2IOModConfigDigOutputEntry.setStatus(_A)
class _Hm2IOModConfigDigOutputModID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2IOModConfigDigOutputModID_Type.__name__=_B
_Hm2IOModConfigDigOutputModID_Object=MibTableColumn
hm2IOModConfigDigOutputModID=_Hm2IOModConfigDigOutputModID_Object((1,3,6,1,4,1,248,11,100,1,1,3,1,1),_Hm2IOModConfigDigOutputModID_Type())
hm2IOModConfigDigOutputModID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2IOModConfigDigOutputModID.setStatus(_A)
class _Hm2IOModConfigDigOutputID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2IOModConfigDigOutputID_Type.__name__=_B
_Hm2IOModConfigDigOutputID_Object=MibTableColumn
hm2IOModConfigDigOutputID=_Hm2IOModConfigDigOutputID_Object((1,3,6,1,4,1,248,11,100,1,1,3,1,2),_Hm2IOModConfigDigOutputID_Type())
hm2IOModConfigDigOutputID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2IOModConfigDigOutputID.setStatus(_A)
class _Hm2IOModConfigDigOutputLogEvent_Type(HmEnabledStatus):defaultValue=2
_Hm2IOModConfigDigOutputLogEvent_Type.__name__=_F
_Hm2IOModConfigDigOutputLogEvent_Object=MibTableColumn
hm2IOModConfigDigOutputLogEvent=_Hm2IOModConfigDigOutputLogEvent_Object((1,3,6,1,4,1,248,11,100,1,1,3,1,3),_Hm2IOModConfigDigOutputLogEvent_Type())
hm2IOModConfigDigOutputLogEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigOutputLogEvent.setStatus(_A)
class _Hm2IOModConfigDigOutputSnmpTrap_Type(HmEnabledStatus):defaultValue=2
_Hm2IOModConfigDigOutputSnmpTrap_Type.__name__=_F
_Hm2IOModConfigDigOutputSnmpTrap_Object=MibTableColumn
hm2IOModConfigDigOutputSnmpTrap=_Hm2IOModConfigDigOutputSnmpTrap_Object((1,3,6,1,4,1,248,11,100,1,1,3,1,4),_Hm2IOModConfigDigOutputSnmpTrap_Type())
hm2IOModConfigDigOutputSnmpTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigOutputSnmpTrap.setStatus(_A)
class _Hm2IOModConfigDigOutputSourceAddressType_Type(InetAddressType):defaultValue=1
_Hm2IOModConfigDigOutputSourceAddressType_Type.__name__=_H
_Hm2IOModConfigDigOutputSourceAddressType_Object=MibTableColumn
hm2IOModConfigDigOutputSourceAddressType=_Hm2IOModConfigDigOutputSourceAddressType_Object((1,3,6,1,4,1,248,11,100,1,1,3,1,5),_Hm2IOModConfigDigOutputSourceAddressType_Type())
hm2IOModConfigDigOutputSourceAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigOutputSourceAddressType.setStatus(_A)
class _Hm2IOModConfigDigOutputSourceAddress_Type(InetAddress):defaultHexValue='00000000'
_Hm2IOModConfigDigOutputSourceAddress_Type.__name__=_G
_Hm2IOModConfigDigOutputSourceAddress_Object=MibTableColumn
hm2IOModConfigDigOutputSourceAddress=_Hm2IOModConfigDigOutputSourceAddress_Object((1,3,6,1,4,1,248,11,100,1,1,3,1,6),_Hm2IOModConfigDigOutputSourceAddress_Type())
hm2IOModConfigDigOutputSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigOutputSourceAddress.setStatus(_A)
class _Hm2IOModConfigDigOutputSourcePort_Type(InetPortNumber):defaultValue=161
_Hm2IOModConfigDigOutputSourcePort_Type.__name__=_I
_Hm2IOModConfigDigOutputSourcePort_Object=MibTableColumn
hm2IOModConfigDigOutputSourcePort=_Hm2IOModConfigDigOutputSourcePort_Object((1,3,6,1,4,1,248,11,100,1,1,3,1,7),_Hm2IOModConfigDigOutputSourcePort_Type())
hm2IOModConfigDigOutputSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigOutputSourcePort.setStatus(_A)
class _Hm2IOModConfigDigOutputSourceModID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2IOModConfigDigOutputSourceModID_Type.__name__=_B
_Hm2IOModConfigDigOutputSourceModID_Object=MibTableColumn
hm2IOModConfigDigOutputSourceModID=_Hm2IOModConfigDigOutputSourceModID_Object((1,3,6,1,4,1,248,11,100,1,1,3,1,8),_Hm2IOModConfigDigOutputSourceModID_Type())
hm2IOModConfigDigOutputSourceModID.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigOutputSourceModID.setStatus(_A)
class _Hm2IOModConfigDigOutputSourceID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2IOModConfigDigOutputSourceID_Type.__name__=_B
_Hm2IOModConfigDigOutputSourceID_Object=MibTableColumn
hm2IOModConfigDigOutputSourceID=_Hm2IOModConfigDigOutputSourceID_Object((1,3,6,1,4,1,248,11,100,1,1,3,1,9),_Hm2IOModConfigDigOutputSourceID_Type())
hm2IOModConfigDigOutputSourceID.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2IOModConfigDigOutputSourceID.setStatus(_A)
_Hm2IOModValueGroup_ObjectIdentity=ObjectIdentity
hm2IOModValueGroup=_Hm2IOModValueGroup_ObjectIdentity((1,3,6,1,4,1,248,11,100,1,2))
_Hm2IOModValueDigInputTable_Object=MibTable
hm2IOModValueDigInputTable=_Hm2IOModValueDigInputTable_Object((1,3,6,1,4,1,248,11,100,1,2,1))
if mibBuilder.loadTexts:hm2IOModValueDigInputTable.setStatus(_A)
_Hm2IOModValueDigInputEntry_Object=MibTableRow
hm2IOModValueDigInputEntry=_Hm2IOModValueDigInputEntry_Object((1,3,6,1,4,1,248,11,100,1,2,1,1))
hm2IOModValueDigInputEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:hm2IOModValueDigInputEntry.setStatus(_A)
class _Hm2IOModValueDigInputModID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2IOModValueDigInputModID_Type.__name__=_B
_Hm2IOModValueDigInputModID_Object=MibTableColumn
hm2IOModValueDigInputModID=_Hm2IOModValueDigInputModID_Object((1,3,6,1,4,1,248,11,100,1,2,1,1,1),_Hm2IOModValueDigInputModID_Type())
hm2IOModValueDigInputModID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2IOModValueDigInputModID.setStatus(_A)
class _Hm2IOModValueDigInputID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2IOModValueDigInputID_Type.__name__=_B
_Hm2IOModValueDigInputID_Object=MibTableColumn
hm2IOModValueDigInputID=_Hm2IOModValueDigInputID_Object((1,3,6,1,4,1,248,11,100,1,2,1,1,2),_Hm2IOModValueDigInputID_Type())
hm2IOModValueDigInputID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2IOModValueDigInputID.setStatus(_A)
class _Hm2IOModValueDigInputValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),('high',1),('low',2)))
_Hm2IOModValueDigInputValue_Type.__name__=_B
_Hm2IOModValueDigInputValue_Object=MibTableColumn
hm2IOModValueDigInputValue=_Hm2IOModValueDigInputValue_Object((1,3,6,1,4,1,248,11,100,1,2,1,1,3),_Hm2IOModValueDigInputValue_Type())
hm2IOModValueDigInputValue.setMaxAccess(_Q)
if mibBuilder.loadTexts:hm2IOModValueDigInputValue.setStatus(_A)
_Hm2IOModValueDigOutputTable_Object=MibTable
hm2IOModValueDigOutputTable=_Hm2IOModValueDigOutputTable_Object((1,3,6,1,4,1,248,11,100,1,2,2))
if mibBuilder.loadTexts:hm2IOModValueDigOutputTable.setStatus(_A)
_Hm2IOModValueDigOutputEntry_Object=MibTableRow
hm2IOModValueDigOutputEntry=_Hm2IOModValueDigOutputEntry_Object((1,3,6,1,4,1,248,11,100,1,2,2,1))
hm2IOModValueDigOutputEntry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:hm2IOModValueDigOutputEntry.setStatus(_A)
class _Hm2IOModValueDigOutputModID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2IOModValueDigOutputModID_Type.__name__=_B
_Hm2IOModValueDigOutputModID_Object=MibTableColumn
hm2IOModValueDigOutputModID=_Hm2IOModValueDigOutputModID_Object((1,3,6,1,4,1,248,11,100,1,2,2,1,1),_Hm2IOModValueDigOutputModID_Type())
hm2IOModValueDigOutputModID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2IOModValueDigOutputModID.setStatus(_A)
class _Hm2IOModValueDigOutputID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2IOModValueDigOutputID_Type.__name__=_B
_Hm2IOModValueDigOutputID_Object=MibTableColumn
hm2IOModValueDigOutputID=_Hm2IOModValueDigOutputID_Object((1,3,6,1,4,1,248,11,100,1,2,2,1,2),_Hm2IOModValueDigOutputID_Type())
hm2IOModValueDigOutputID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2IOModValueDigOutputID.setStatus(_A)
class _Hm2IOModValueDigOutputValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_P,0),('high',1),('low',2),('invalid',3),('not-configured',4)))
_Hm2IOModValueDigOutputValue_Type.__name__=_B
_Hm2IOModValueDigOutputValue_Object=MibTableColumn
hm2IOModValueDigOutputValue=_Hm2IOModValueDigOutputValue_Object((1,3,6,1,4,1,248,11,100,1,2,2,1,3),_Hm2IOModValueDigOutputValue_Type())
hm2IOModValueDigOutputValue.setMaxAccess(_Q)
if mibBuilder.loadTexts:hm2IOModValueDigOutputValue.setStatus(_A)
hm2IOModDigInputChangeTrap=NotificationType((1,3,6,1,4,1,248,11,100,0,1))
hm2IOModDigInputChangeTrap.setObjects((_D,_T))
if mibBuilder.loadTexts:hm2IOModDigInputChangeTrap.setStatus(_A)
hm2IOModDigOutputChangeTrap=NotificationType((1,3,6,1,4,1,248,11,100,0,2))
hm2IOModDigOutputChangeTrap.setObjects((_D,_U))
if mibBuilder.loadTexts:hm2IOModDigOutputChangeTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hm2IOModuleMib':hm2IOModuleMib,'hm2IOModuleMibNotifications':hm2IOModuleMibNotifications,'hm2IOModDigInputChangeTrap':hm2IOModDigInputChangeTrap,'hm2IOModDigOutputChangeTrap':hm2IOModDigOutputChangeTrap,'hm2IOModuleMibObjects':hm2IOModuleMibObjects,'hm2IOModConfigGroup':hm2IOModConfigGroup,'hm2IOModConfigCommon':hm2IOModConfigCommon,'hm2IOModConfigDigInputAdminState':hm2IOModConfigDigInputAdminState,'hm2IOModConfigDigOutputAdminState':hm2IOModConfigDigOutputAdminState,'hm2IOModConfigDigInputRefreshInterval':hm2IOModConfigDigInputRefreshInterval,'hm2IOModConfigDigOutputRefreshInterval':hm2IOModConfigDigOutputRefreshInterval,'hm2IOModConfigDigOutputRetryCount':hm2IOModConfigDigOutputRetryCount,'hm2IOModConfigDigInputTable':hm2IOModConfigDigInputTable,'hm2IOModConfigDigInputEntry':hm2IOModConfigDigInputEntry,_J:hm2IOModConfigDigInputModID,_K:hm2IOModConfigDigInputID,'hm2IOModConfigDigInputLogEvent':hm2IOModConfigDigInputLogEvent,'hm2IOModConfigDigInputSnmpTrap':hm2IOModConfigDigInputSnmpTrap,'hm2IOModConfigDigOutputTable':hm2IOModConfigDigOutputTable,'hm2IOModConfigDigOutputEntry':hm2IOModConfigDigOutputEntry,_L:hm2IOModConfigDigOutputModID,_M:hm2IOModConfigDigOutputID,'hm2IOModConfigDigOutputLogEvent':hm2IOModConfigDigOutputLogEvent,'hm2IOModConfigDigOutputSnmpTrap':hm2IOModConfigDigOutputSnmpTrap,'hm2IOModConfigDigOutputSourceAddressType':hm2IOModConfigDigOutputSourceAddressType,'hm2IOModConfigDigOutputSourceAddress':hm2IOModConfigDigOutputSourceAddress,'hm2IOModConfigDigOutputSourcePort':hm2IOModConfigDigOutputSourcePort,'hm2IOModConfigDigOutputSourceModID':hm2IOModConfigDigOutputSourceModID,'hm2IOModConfigDigOutputSourceID':hm2IOModConfigDigOutputSourceID,'hm2IOModValueGroup':hm2IOModValueGroup,'hm2IOModValueDigInputTable':hm2IOModValueDigInputTable,'hm2IOModValueDigInputEntry':hm2IOModValueDigInputEntry,_N:hm2IOModValueDigInputModID,_O:hm2IOModValueDigInputID,_T:hm2IOModValueDigInputValue,'hm2IOModValueDigOutputTable':hm2IOModValueDigOutputTable,'hm2IOModValueDigOutputEntry':hm2IOModValueDigOutputEntry,_R:hm2IOModValueDigOutputModID,_S:hm2IOModValueDigOutputID,_U:hm2IOModValueDigOutputValue})