_A3='pdnNetToMediaParamsAprTimeToNextGroup'
_A2='pdnNetToMediaParamsAprConfigGroup'
_A1='pdnNetToMediaUnauthorizedUserEventGroup'
_A0='pdnNetToMediaLimitGroup'
_z='pdnNetToMediaExtGroup'
_y='pdnNetToMediaConfigProxyArpGroup'
_x='pdnNetToMediaProxyArpGroup'
_w='pdnNetToMediaClearGroup'
_v='pdnNetToMedia8023ConfigGroup'
_u='pdnNetToMediaConfigGroup'
_t='pdnNetToMediaParamsGroup'
_s='unauthorizedUserEvent'
_r='pdnNetToMediaParamsAprTimeToNext'
_q='pdnNetToMediaParamsAprReqPeriod'
_p='pdnNetToMediaParamsAprRowStatus'
_o='ipNetToMediaMaxIPAddresses'
_n='ipNetToMediaLimitEnabled'
_m='ipNetToMediaNHR'
_l='ipNetToMediaDefaultNHR'
_k='ipNetToMediaForwardingMode'
_j='pdnNetToMediaProxyArpStatus'
_i='pdnNetToMediaClearAllArp'
_h='pdnNetTo8023MediaConfigRowStatus'
_g='pdnNetTo8023MediaConfigPerm'
_f='pdnNetTo8023MediaConfigTrailer'
_e='pdnNetTo8023MediaConfigFlags'
_d='pdnNetTo8023MediaConfigMin'
_c='pdnNetTo8023MediaConfigMacAddr'
_b='pdnNetToMediaConfigRowStatus'
_a='pdnNetToMediaConfigPerm'
_Z='pdnNetToMediaConfigTrailer'
_Y='pdnNetToMediaConfigFlags'
_X='pdnNetToMediaConfigMin'
_W='pdnNetToMediaConfigMacAddr'
_V='pdnNetToMediaParamsDefRouteEntryTimeout'
_U='pdnNetToMediaParamsIncompEntryTimeout'
_T='pdnNetToMediaParamsCompEntryTimeout'
_S='ipNetToMediaExtEntry'
_R='pdnNetTo8023MediaConfigIpAddr'
_Q='pdnNetToMediaConfigIpAddr'
_P='minutes'
_O='pdnNetToMediaParamsAprIpAddr'
_N='Unsigned32'
_M='ipNetToMediaPhysAddress'
_L='pdnNetTo8023MediaConfigVnidId'
_K='not-accessible'
_J='ipNetToMediaIfIndex'
_I='IP-MIB'
_H='ifIndex'
_G='IF-MIB'
_F='read-only'
_E='read-write'
_D='Integer32'
_C='read-create'
_B='PDN-ARP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ipNetToMediaEntry,ipNetToMediaIfIndex,ipNetToMediaPhysAddress=mibBuilder.importSymbols(_I,'ipNetToMediaEntry',_J,_M)
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
SwitchState,VnidRange=mibBuilder.importSymbols('PDN-TC','SwitchState','VnidRange')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
pdn_arp=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,27))
if mibBuilder.loadTexts:pdn_arp.setRevisions(('2005-07-19 00:00','2002-08-02 00:00','2002-04-18 00:00','2001-12-31 00:00','2001-01-15 00:00','2000-05-02 00:00'))
_PdnNetToMediaGenericMIBObjects_ObjectIdentity=ObjectIdentity
pdnNetToMediaGenericMIBObjects=_PdnNetToMediaGenericMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,27,1))
_PdnNetToMediaParams_ObjectIdentity=ObjectIdentity
pdnNetToMediaParams=_PdnNetToMediaParams_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,27,1,1))
class _PdnNetToMediaParamsCompEntryTimeout_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_PdnNetToMediaParamsCompEntryTimeout_Type.__name__=_D
_PdnNetToMediaParamsCompEntryTimeout_Object=MibScalar
pdnNetToMediaParamsCompEntryTimeout=_PdnNetToMediaParamsCompEntryTimeout_Object((1,3,6,1,4,1,1795,2,24,2,27,1,1,1),_PdnNetToMediaParamsCompEntryTimeout_Type())
pdnNetToMediaParamsCompEntryTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnNetToMediaParamsCompEntryTimeout.setStatus(_A)
class _PdnNetToMediaParamsIncompEntryTimeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_PdnNetToMediaParamsIncompEntryTimeout_Type.__name__=_D
_PdnNetToMediaParamsIncompEntryTimeout_Object=MibScalar
pdnNetToMediaParamsIncompEntryTimeout=_PdnNetToMediaParamsIncompEntryTimeout_Object((1,3,6,1,4,1,1795,2,24,2,27,1,1,2),_PdnNetToMediaParamsIncompEntryTimeout_Type())
pdnNetToMediaParamsIncompEntryTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnNetToMediaParamsIncompEntryTimeout.setStatus(_A)
class _PdnNetToMediaParamsDefRouteEntryTimeout_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_PdnNetToMediaParamsDefRouteEntryTimeout_Type.__name__=_D
_PdnNetToMediaParamsDefRouteEntryTimeout_Object=MibScalar
pdnNetToMediaParamsDefRouteEntryTimeout=_PdnNetToMediaParamsDefRouteEntryTimeout_Object((1,3,6,1,4,1,1795,2,24,2,27,1,1,3),_PdnNetToMediaParamsDefRouteEntryTimeout_Type())
pdnNetToMediaParamsDefRouteEntryTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnNetToMediaParamsDefRouteEntryTimeout.setStatus(_A)
_PdnNetToMediaParamsAprTable_Object=MibTable
pdnNetToMediaParamsAprTable=_PdnNetToMediaParamsAprTable_Object((1,3,6,1,4,1,1795,2,24,2,27,1,1,4))
if mibBuilder.loadTexts:pdnNetToMediaParamsAprTable.setStatus(_A)
_PdnNetToMediaParamsAprEntry_Object=MibTableRow
pdnNetToMediaParamsAprEntry=_PdnNetToMediaParamsAprEntry_Object((1,3,6,1,4,1,1795,2,24,2,27,1,1,4,1))
pdnNetToMediaParamsAprEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:pdnNetToMediaParamsAprEntry.setStatus(_A)
_PdnNetToMediaParamsAprIpAddr_Type=IpAddress
_PdnNetToMediaParamsAprIpAddr_Object=MibTableColumn
pdnNetToMediaParamsAprIpAddr=_PdnNetToMediaParamsAprIpAddr_Object((1,3,6,1,4,1,1795,2,24,2,27,1,1,4,1,1),_PdnNetToMediaParamsAprIpAddr_Type())
pdnNetToMediaParamsAprIpAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:pdnNetToMediaParamsAprIpAddr.setStatus(_A)
_PdnNetToMediaParamsAprRowStatus_Type=RowStatus
_PdnNetToMediaParamsAprRowStatus_Object=MibTableColumn
pdnNetToMediaParamsAprRowStatus=_PdnNetToMediaParamsAprRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,27,1,1,4,1,2),_PdnNetToMediaParamsAprRowStatus_Type())
pdnNetToMediaParamsAprRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnNetToMediaParamsAprRowStatus.setStatus(_A)
class _PdnNetToMediaParamsAprReqPeriod_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_PdnNetToMediaParamsAprReqPeriod_Type.__name__=_N
_PdnNetToMediaParamsAprReqPeriod_Object=MibTableColumn
pdnNetToMediaParamsAprReqPeriod=_PdnNetToMediaParamsAprReqPeriod_Object((1,3,6,1,4,1,1795,2,24,2,27,1,1,4,1,3),_PdnNetToMediaParamsAprReqPeriod_Type())
pdnNetToMediaParamsAprReqPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnNetToMediaParamsAprReqPeriod.setStatus(_A)
if mibBuilder.loadTexts:pdnNetToMediaParamsAprReqPeriod.setUnits(_P)
_PdnNetToMediaParamsAprTimeToNext_Type=Unsigned32
_PdnNetToMediaParamsAprTimeToNext_Object=MibTableColumn
pdnNetToMediaParamsAprTimeToNext=_PdnNetToMediaParamsAprTimeToNext_Object((1,3,6,1,4,1,1795,2,24,2,27,1,1,4,1,4),_PdnNetToMediaParamsAprTimeToNext_Type())
pdnNetToMediaParamsAprTimeToNext.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnNetToMediaParamsAprTimeToNext.setStatus(_A)
if mibBuilder.loadTexts:pdnNetToMediaParamsAprTimeToNext.setUnits(_P)
_PdnNetToMediaConfig_ObjectIdentity=ObjectIdentity
pdnNetToMediaConfig=_PdnNetToMediaConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,27,1,2))
_PdnNetToMediaConfigTable_Object=MibTable
pdnNetToMediaConfigTable=_PdnNetToMediaConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,1))
if mibBuilder.loadTexts:pdnNetToMediaConfigTable.setStatus(_A)
_PdnNetToMediaConfigEntry_Object=MibTableRow
pdnNetToMediaConfigEntry=_PdnNetToMediaConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,1,1))
pdnNetToMediaConfigEntry.setIndexNames((0,_G,_H),(0,_B,_Q))
if mibBuilder.loadTexts:pdnNetToMediaConfigEntry.setStatus(_A)
_PdnNetToMediaConfigIpAddr_Type=IpAddress
_PdnNetToMediaConfigIpAddr_Object=MibTableColumn
pdnNetToMediaConfigIpAddr=_PdnNetToMediaConfigIpAddr_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,1,1,1),_PdnNetToMediaConfigIpAddr_Type())
pdnNetToMediaConfigIpAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:pdnNetToMediaConfigIpAddr.setStatus(_A)
_PdnNetToMediaConfigMacAddr_Type=MacAddress
_PdnNetToMediaConfigMacAddr_Object=MibTableColumn
pdnNetToMediaConfigMacAddr=_PdnNetToMediaConfigMacAddr_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,1,1,2),_PdnNetToMediaConfigMacAddr_Type())
pdnNetToMediaConfigMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnNetToMediaConfigMacAddr.setStatus(_A)
class _PdnNetToMediaConfigMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_PdnNetToMediaConfigMin_Type.__name__=_D
_PdnNetToMediaConfigMin_Object=MibTableColumn
pdnNetToMediaConfigMin=_PdnNetToMediaConfigMin_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,1,1,3),_PdnNetToMediaConfigMin_Type())
pdnNetToMediaConfigMin.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnNetToMediaConfigMin.setStatus(_A)
_PdnNetToMediaConfigFlags_Type=Integer32
_PdnNetToMediaConfigFlags_Object=MibTableColumn
pdnNetToMediaConfigFlags=_PdnNetToMediaConfigFlags_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,1,1,4),_PdnNetToMediaConfigFlags_Type())
pdnNetToMediaConfigFlags.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnNetToMediaConfigFlags.setStatus(_A)
_PdnNetToMediaConfigTrailer_Type=SwitchState
_PdnNetToMediaConfigTrailer_Object=MibTableColumn
pdnNetToMediaConfigTrailer=_PdnNetToMediaConfigTrailer_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,1,1,5),_PdnNetToMediaConfigTrailer_Type())
pdnNetToMediaConfigTrailer.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnNetToMediaConfigTrailer.setStatus(_A)
_PdnNetToMediaConfigPerm_Type=TruthValue
_PdnNetToMediaConfigPerm_Object=MibTableColumn
pdnNetToMediaConfigPerm=_PdnNetToMediaConfigPerm_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,1,1,6),_PdnNetToMediaConfigPerm_Type())
pdnNetToMediaConfigPerm.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnNetToMediaConfigPerm.setStatus(_A)
_PdnNetToMediaConfigRowStatus_Type=RowStatus
_PdnNetToMediaConfigRowStatus_Object=MibTableColumn
pdnNetToMediaConfigRowStatus=_PdnNetToMediaConfigRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,1,1,7),_PdnNetToMediaConfigRowStatus_Type())
pdnNetToMediaConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnNetToMediaConfigRowStatus.setStatus(_A)
class _PdnNetToMediaClearAllArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noop',1),('clear',2)))
_PdnNetToMediaClearAllArp_Type.__name__=_D
_PdnNetToMediaClearAllArp_Object=MibScalar
pdnNetToMediaClearAllArp=_PdnNetToMediaClearAllArp_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,2),_PdnNetToMediaClearAllArp_Type())
pdnNetToMediaClearAllArp.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnNetToMediaClearAllArp.setStatus(_A)
_PdnNetToMediaProxyArpTable_Object=MibTable
pdnNetToMediaProxyArpTable=_PdnNetToMediaProxyArpTable_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,3))
if mibBuilder.loadTexts:pdnNetToMediaProxyArpTable.setStatus(_A)
_PdnNetToMediaProxyArpEntry_Object=MibTableRow
pdnNetToMediaProxyArpEntry=_PdnNetToMediaProxyArpEntry_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,3,1))
pdnNetToMediaProxyArpEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pdnNetToMediaProxyArpEntry.setStatus(_A)
class _PdnNetToMediaProxyArpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_PdnNetToMediaProxyArpStatus_Type.__name__=_D
_PdnNetToMediaProxyArpStatus_Object=MibTableColumn
pdnNetToMediaProxyArpStatus=_PdnNetToMediaProxyArpStatus_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,3,1,1),_PdnNetToMediaProxyArpStatus_Type())
pdnNetToMediaProxyArpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnNetToMediaProxyArpStatus.setStatus(_A)
_IpNetToMediaConfig_ObjectIdentity=ObjectIdentity
ipNetToMediaConfig=_IpNetToMediaConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,27,1,2,4))
class _IpNetToMediaForwardingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('basic',1),('mux',2),('sms',3),('ult',4),('vlan',5)))
_IpNetToMediaForwardingMode_Type.__name__=_D
_IpNetToMediaForwardingMode_Object=MibScalar
ipNetToMediaForwardingMode=_IpNetToMediaForwardingMode_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,4,1),_IpNetToMediaForwardingMode_Type())
ipNetToMediaForwardingMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ipNetToMediaForwardingMode.setStatus(_A)
_IpNetToMediaDefaultNHR_Type=IpAddress
_IpNetToMediaDefaultNHR_Object=MibScalar
ipNetToMediaDefaultNHR=_IpNetToMediaDefaultNHR_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,4,2),_IpNetToMediaDefaultNHR_Type())
ipNetToMediaDefaultNHR.setMaxAccess(_E)
if mibBuilder.loadTexts:ipNetToMediaDefaultNHR.setStatus(_A)
_IpNetToMediaExtTable_Object=MibTable
ipNetToMediaExtTable=_IpNetToMediaExtTable_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,4,3))
if mibBuilder.loadTexts:ipNetToMediaExtTable.setStatus(_A)
_IpNetToMediaExtEntry_Object=MibTableRow
ipNetToMediaExtEntry=_IpNetToMediaExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,4,3,1))
if mibBuilder.loadTexts:ipNetToMediaExtEntry.setStatus(_A)
_IpNetToMediaNHR_Type=IpAddress
_IpNetToMediaNHR_Object=MibTableColumn
ipNetToMediaNHR=_IpNetToMediaNHR_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,4,3,1,1),_IpNetToMediaNHR_Type())
ipNetToMediaNHR.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetToMediaNHR.setStatus(_A)
_IpNetToMediaLimitTable_Object=MibTable
ipNetToMediaLimitTable=_IpNetToMediaLimitTable_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,4,4))
if mibBuilder.loadTexts:ipNetToMediaLimitTable.setStatus(_A)
_IpNetToMediaLimitEntry_Object=MibTableRow
ipNetToMediaLimitEntry=_IpNetToMediaLimitEntry_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,4,4,1))
ipNetToMediaLimitEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:ipNetToMediaLimitEntry.setStatus(_A)
_IpNetToMediaLimitEnabled_Type=TruthValue
_IpNetToMediaLimitEnabled_Object=MibTableColumn
ipNetToMediaLimitEnabled=_IpNetToMediaLimitEnabled_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,4,4,1,1),_IpNetToMediaLimitEnabled_Type())
ipNetToMediaLimitEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetToMediaLimitEnabled.setStatus(_A)
class _IpNetToMediaMaxIPAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_IpNetToMediaMaxIPAddresses_Type.__name__=_D
_IpNetToMediaMaxIPAddresses_Object=MibTableColumn
ipNetToMediaMaxIPAddresses=_IpNetToMediaMaxIPAddresses_Object((1,3,6,1,4,1,1795,2,24,2,27,1,2,4,4,1,2),_IpNetToMediaMaxIPAddresses_Type())
ipNetToMediaMaxIPAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetToMediaMaxIPAddresses.setStatus(_A)
_PdnNetTo8023MediaConfig_ObjectIdentity=ObjectIdentity
pdnNetTo8023MediaConfig=_PdnNetTo8023MediaConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,27,1,3))
_PdnNetTo8023MediaConfigTable_Object=MibTable
pdnNetTo8023MediaConfigTable=_PdnNetTo8023MediaConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,27,1,3,1))
if mibBuilder.loadTexts:pdnNetTo8023MediaConfigTable.setStatus(_A)
_PdnNetTo8023MediaConfigEntry_Object=MibTableRow
pdnNetTo8023MediaConfigEntry=_PdnNetTo8023MediaConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,27,1,3,1,1))
pdnNetTo8023MediaConfigEntry.setIndexNames((0,_G,_H),(0,_B,_R),(0,_B,_L))
if mibBuilder.loadTexts:pdnNetTo8023MediaConfigEntry.setStatus(_A)
_PdnNetTo8023MediaConfigIpAddr_Type=IpAddress
_PdnNetTo8023MediaConfigIpAddr_Object=MibTableColumn
pdnNetTo8023MediaConfigIpAddr=_PdnNetTo8023MediaConfigIpAddr_Object((1,3,6,1,4,1,1795,2,24,2,27,1,3,1,1,1),_PdnNetTo8023MediaConfigIpAddr_Type())
pdnNetTo8023MediaConfigIpAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:pdnNetTo8023MediaConfigIpAddr.setStatus(_A)
_PdnNetTo8023MediaConfigVnidId_Type=VnidRange
_PdnNetTo8023MediaConfigVnidId_Object=MibTableColumn
pdnNetTo8023MediaConfigVnidId=_PdnNetTo8023MediaConfigVnidId_Object((1,3,6,1,4,1,1795,2,24,2,27,1,3,1,1,2),_PdnNetTo8023MediaConfigVnidId_Type())
pdnNetTo8023MediaConfigVnidId.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnNetTo8023MediaConfigVnidId.setStatus(_A)
_PdnNetTo8023MediaConfigMacAddr_Type=MacAddress
_PdnNetTo8023MediaConfigMacAddr_Object=MibTableColumn
pdnNetTo8023MediaConfigMacAddr=_PdnNetTo8023MediaConfigMacAddr_Object((1,3,6,1,4,1,1795,2,24,2,27,1,3,1,1,3),_PdnNetTo8023MediaConfigMacAddr_Type())
pdnNetTo8023MediaConfigMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnNetTo8023MediaConfigMacAddr.setStatus(_A)
class _PdnNetTo8023MediaConfigMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_PdnNetTo8023MediaConfigMin_Type.__name__=_D
_PdnNetTo8023MediaConfigMin_Object=MibTableColumn
pdnNetTo8023MediaConfigMin=_PdnNetTo8023MediaConfigMin_Object((1,3,6,1,4,1,1795,2,24,2,27,1,3,1,1,4),_PdnNetTo8023MediaConfigMin_Type())
pdnNetTo8023MediaConfigMin.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnNetTo8023MediaConfigMin.setStatus(_A)
_PdnNetTo8023MediaConfigFlags_Type=Integer32
_PdnNetTo8023MediaConfigFlags_Object=MibTableColumn
pdnNetTo8023MediaConfigFlags=_PdnNetTo8023MediaConfigFlags_Object((1,3,6,1,4,1,1795,2,24,2,27,1,3,1,1,5),_PdnNetTo8023MediaConfigFlags_Type())
pdnNetTo8023MediaConfigFlags.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnNetTo8023MediaConfigFlags.setStatus(_A)
_PdnNetTo8023MediaConfigTrailer_Type=SwitchState
_PdnNetTo8023MediaConfigTrailer_Object=MibTableColumn
pdnNetTo8023MediaConfigTrailer=_PdnNetTo8023MediaConfigTrailer_Object((1,3,6,1,4,1,1795,2,24,2,27,1,3,1,1,6),_PdnNetTo8023MediaConfigTrailer_Type())
pdnNetTo8023MediaConfigTrailer.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnNetTo8023MediaConfigTrailer.setStatus(_A)
_PdnNetTo8023MediaConfigPerm_Type=TruthValue
_PdnNetTo8023MediaConfigPerm_Object=MibTableColumn
pdnNetTo8023MediaConfigPerm=_PdnNetTo8023MediaConfigPerm_Object((1,3,6,1,4,1,1795,2,24,2,27,1,3,1,1,7),_PdnNetTo8023MediaConfigPerm_Type())
pdnNetTo8023MediaConfigPerm.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnNetTo8023MediaConfigPerm.setStatus(_A)
_PdnNetTo8023MediaConfigRowStatus_Type=RowStatus
_PdnNetTo8023MediaConfigRowStatus_Object=MibTableColumn
pdnNetTo8023MediaConfigRowStatus=_PdnNetTo8023MediaConfigRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,27,1,3,1,1,8),_PdnNetTo8023MediaConfigRowStatus_Type())
pdnNetTo8023MediaConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnNetTo8023MediaConfigRowStatus.setStatus(_A)
_PdnNetToMediaConformance_ObjectIdentity=ObjectIdentity
pdnNetToMediaConformance=_PdnNetToMediaConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,27,1,4))
_PdnNetToMediaCompliances_ObjectIdentity=ObjectIdentity
pdnNetToMediaCompliances=_PdnNetToMediaCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,27,1,4,1))
_PdnNetToMediaGroups_ObjectIdentity=ObjectIdentity
pdnNetToMediaGroups=_PdnNetToMediaGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,27,1,4,2))
_PdnNetToMediaObjGroups_ObjectIdentity=ObjectIdentity
pdnNetToMediaObjGroups=_PdnNetToMediaObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,1))
_PdnNetToMediaNtfyGroups_ObjectIdentity=ObjectIdentity
pdnNetToMediaNtfyGroups=_PdnNetToMediaNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,2))
_PdnNetToMediaMIBTraps_ObjectIdentity=ObjectIdentity
pdnNetToMediaMIBTraps=_PdnNetToMediaMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,27,2))
_PdnNetToMediaMIBNotifications_ObjectIdentity=ObjectIdentity
pdnNetToMediaMIBNotifications=_PdnNetToMediaMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,27,2,0))
ipNetToMediaEntry.registerAugmentions((_B,_S))
ipNetToMediaExtEntry.setIndexNames(*ipNetToMediaEntry.getIndexNames())
pdnNetToMediaParamsGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,1,1))
pdnNetToMediaParamsGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:pdnNetToMediaParamsGroup.setStatus(_A)
pdnNetToMediaConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,1,2))
pdnNetToMediaConfigGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:pdnNetToMediaConfigGroup.setStatus(_A)
pdnNetToMedia8023ConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,1,3))
pdnNetToMedia8023ConfigGroup.setObjects(*((_B,_L),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:pdnNetToMedia8023ConfigGroup.setStatus(_A)
pdnNetToMediaClearGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,1,4))
pdnNetToMediaClearGroup.setObjects((_B,_i))
if mibBuilder.loadTexts:pdnNetToMediaClearGroup.setStatus(_A)
pdnNetToMediaProxyArpGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,1,5))
pdnNetToMediaProxyArpGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:pdnNetToMediaProxyArpGroup.setStatus(_A)
pdnNetToMediaConfigProxyArpGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,1,6))
pdnNetToMediaConfigProxyArpGroup.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:pdnNetToMediaConfigProxyArpGroup.setStatus(_A)
pdnNetToMediaExtGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,1,7))
pdnNetToMediaExtGroup.setObjects((_B,_m))
if mibBuilder.loadTexts:pdnNetToMediaExtGroup.setStatus(_A)
pdnNetToMediaLimitGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,1,8))
pdnNetToMediaLimitGroup.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:pdnNetToMediaLimitGroup.setStatus(_A)
pdnNetToMediaParamsAprConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,1,9))
pdnNetToMediaParamsAprConfigGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:pdnNetToMediaParamsAprConfigGroup.setStatus(_A)
pdnNetToMediaParamsAprTimeToNextGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,1,10))
pdnNetToMediaParamsAprTimeToNextGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:pdnNetToMediaParamsAprTimeToNextGroup.setStatus(_A)
unauthorizedUserEvent=NotificationType((1,3,6,1,4,1,1795,2,24,2,27,2,0,1))
unauthorizedUserEvent.setObjects(*((_I,_J),(_I,_M)))
if mibBuilder.loadTexts:unauthorizedUserEvent.setStatus(_A)
pdnNetToMediaUnauthorizedUserEventGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,2,27,1,4,2,2,1))
pdnNetToMediaUnauthorizedUserEventGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:pdnNetToMediaUnauthorizedUserEventGroup.setStatus(_A)
pdnNetToMediaCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,27,1,4,1,1))
pdnNetToMediaCompliance.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:pdnNetToMediaCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdn-arp':pdn_arp,'pdnNetToMediaGenericMIBObjects':pdnNetToMediaGenericMIBObjects,'pdnNetToMediaParams':pdnNetToMediaParams,_T:pdnNetToMediaParamsCompEntryTimeout,_U:pdnNetToMediaParamsIncompEntryTimeout,_V:pdnNetToMediaParamsDefRouteEntryTimeout,'pdnNetToMediaParamsAprTable':pdnNetToMediaParamsAprTable,'pdnNetToMediaParamsAprEntry':pdnNetToMediaParamsAprEntry,_O:pdnNetToMediaParamsAprIpAddr,_p:pdnNetToMediaParamsAprRowStatus,_q:pdnNetToMediaParamsAprReqPeriod,_r:pdnNetToMediaParamsAprTimeToNext,'pdnNetToMediaConfig':pdnNetToMediaConfig,'pdnNetToMediaConfigTable':pdnNetToMediaConfigTable,'pdnNetToMediaConfigEntry':pdnNetToMediaConfigEntry,_Q:pdnNetToMediaConfigIpAddr,_W:pdnNetToMediaConfigMacAddr,_X:pdnNetToMediaConfigMin,_Y:pdnNetToMediaConfigFlags,_Z:pdnNetToMediaConfigTrailer,_a:pdnNetToMediaConfigPerm,_b:pdnNetToMediaConfigRowStatus,_i:pdnNetToMediaClearAllArp,'pdnNetToMediaProxyArpTable':pdnNetToMediaProxyArpTable,'pdnNetToMediaProxyArpEntry':pdnNetToMediaProxyArpEntry,_j:pdnNetToMediaProxyArpStatus,'ipNetToMediaConfig':ipNetToMediaConfig,_k:ipNetToMediaForwardingMode,_l:ipNetToMediaDefaultNHR,'ipNetToMediaExtTable':ipNetToMediaExtTable,_S:ipNetToMediaExtEntry,_m:ipNetToMediaNHR,'ipNetToMediaLimitTable':ipNetToMediaLimitTable,'ipNetToMediaLimitEntry':ipNetToMediaLimitEntry,_n:ipNetToMediaLimitEnabled,_o:ipNetToMediaMaxIPAddresses,'pdnNetTo8023MediaConfig':pdnNetTo8023MediaConfig,'pdnNetTo8023MediaConfigTable':pdnNetTo8023MediaConfigTable,'pdnNetTo8023MediaConfigEntry':pdnNetTo8023MediaConfigEntry,_R:pdnNetTo8023MediaConfigIpAddr,_L:pdnNetTo8023MediaConfigVnidId,_c:pdnNetTo8023MediaConfigMacAddr,_d:pdnNetTo8023MediaConfigMin,_e:pdnNetTo8023MediaConfigFlags,_f:pdnNetTo8023MediaConfigTrailer,_g:pdnNetTo8023MediaConfigPerm,_h:pdnNetTo8023MediaConfigRowStatus,'pdnNetToMediaConformance':pdnNetToMediaConformance,'pdnNetToMediaCompliances':pdnNetToMediaCompliances,'pdnNetToMediaCompliance':pdnNetToMediaCompliance,'pdnNetToMediaGroups':pdnNetToMediaGroups,'pdnNetToMediaObjGroups':pdnNetToMediaObjGroups,_t:pdnNetToMediaParamsGroup,_u:pdnNetToMediaConfigGroup,_v:pdnNetToMedia8023ConfigGroup,_w:pdnNetToMediaClearGroup,_x:pdnNetToMediaProxyArpGroup,_y:pdnNetToMediaConfigProxyArpGroup,_z:pdnNetToMediaExtGroup,_A0:pdnNetToMediaLimitGroup,_A2:pdnNetToMediaParamsAprConfigGroup,_A3:pdnNetToMediaParamsAprTimeToNextGroup,'pdnNetToMediaNtfyGroups':pdnNetToMediaNtfyGroups,_A1:pdnNetToMediaUnauthorizedUserEventGroup,'pdnNetToMediaMIBTraps':pdnNetToMediaMIBTraps,'pdnNetToMediaMIBNotifications':pdnNetToMediaMIBNotifications,_s:unauthorizedUserEvent})