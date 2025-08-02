_P='hpnicfDHCPSvrPoolMacMask'
_O='hpnicfDHCPSvrPoolMac'
_N='hpnicfDHCPSvrOptionCode'
_M='hpnicfDHCPSrvGlbPoolOptCode'
_L='accessible-for-notify'
_K='hpnicfDHCPServerFirstTrapTime'
_J='hpnicfDHCPSvrOptionGroupIndex'
_I='hpnicfDHCPServerPoolName'
_H='hpnicfDHCPSrvGlobalPoolName'
_G='read-create'
_F='OctetString'
_E='read-only'
_D='HPN-ICF-DHCP-SERVER-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
hpnicfDHCPServer=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,101))
if mibBuilder.loadTexts:hpnicfDHCPServer.setRevisions(('2009-05-06 00:00',))
_HpnicfDHCPServerObjects_ObjectIdentity=ObjectIdentity
hpnicfDHCPServerObjects=_HpnicfDHCPServerObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,101,1))
_HpnicfDHCPServerIPPoolUsage_Type=Integer32
_HpnicfDHCPServerIPPoolUsage_Object=MibScalar
hpnicfDHCPServerIPPoolUsage=_HpnicfDHCPServerIPPoolUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,1,1),_HpnicfDHCPServerIPPoolUsage_Type())
hpnicfDHCPServerIPPoolUsage.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPServerIPPoolUsage.setStatus(_A)
_HpnicfDHCPServerReqTimes_Type=Counter32
_HpnicfDHCPServerReqTimes_Object=MibScalar
hpnicfDHCPServerReqTimes=_HpnicfDHCPServerReqTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,1,2),_HpnicfDHCPServerReqTimes_Type())
hpnicfDHCPServerReqTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPServerReqTimes.setStatus(_A)
_HpnicfDHCPServerReqSuccessTimes_Type=Counter32
_HpnicfDHCPServerReqSuccessTimes_Object=MibScalar
hpnicfDHCPServerReqSuccessTimes=_HpnicfDHCPServerReqSuccessTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,1,3),_HpnicfDHCPServerReqSuccessTimes_Type())
hpnicfDHCPServerReqSuccessTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPServerReqSuccessTimes.setStatus(_A)
class _HpnicfDHCPServerAvgIpUseThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDHCPServerAvgIpUseThreshold_Type.__name__=_C
_HpnicfDHCPServerAvgIpUseThreshold_Object=MibScalar
hpnicfDHCPServerAvgIpUseThreshold=_HpnicfDHCPServerAvgIpUseThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,1,4),_HpnicfDHCPServerAvgIpUseThreshold_Type())
hpnicfDHCPServerAvgIpUseThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPServerAvgIpUseThreshold.setStatus(_A)
class _HpnicfDHCPServerMaxIpUseThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDHCPServerMaxIpUseThreshold_Type.__name__=_C
_HpnicfDHCPServerMaxIpUseThreshold_Object=MibScalar
hpnicfDHCPServerMaxIpUseThreshold=_HpnicfDHCPServerMaxIpUseThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,1,5),_HpnicfDHCPServerMaxIpUseThreshold_Type())
hpnicfDHCPServerMaxIpUseThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPServerMaxIpUseThreshold.setStatus(_A)
class _HpnicfDHCPServerAllocateThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDHCPServerAllocateThreshold_Type.__name__=_C
_HpnicfDHCPServerAllocateThreshold_Object=MibScalar
hpnicfDHCPServerAllocateThreshold=_HpnicfDHCPServerAllocateThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,1,6),_HpnicfDHCPServerAllocateThreshold_Type())
hpnicfDHCPServerAllocateThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPServerAllocateThreshold.setStatus(_A)
_HpnicfDHCPServerTables_ObjectIdentity=ObjectIdentity
hpnicfDHCPServerTables=_HpnicfDHCPServerTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,101,2))
class _HpnicfDHCPServerPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDHCPServerPoolName_Type.__name__=_F
_HpnicfDHCPServerPoolName_Object=MibScalar
hpnicfDHCPServerPoolName=_HpnicfDHCPServerPoolName_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,1),_HpnicfDHCPServerPoolName_Type())
hpnicfDHCPServerPoolName.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfDHCPServerPoolName.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolTable_Object=MibTable
hpnicfDHCPSrvGlobalPoolTable=_HpnicfDHCPSrvGlobalPoolTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,2))
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolTable.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolEntry_Object=MibTableRow
hpnicfDHCPSrvGlobalPoolEntry=_HpnicfDHCPSrvGlobalPoolEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,2,1))
hpnicfDHCPSrvGlobalPoolEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolEntry.setStatus(_A)
class _HpnicfDHCPSrvGlobalPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDHCPSrvGlobalPoolName_Type.__name__=_F
_HpnicfDHCPSrvGlobalPoolName_Object=MibTableColumn
hpnicfDHCPSrvGlobalPoolName=_HpnicfDHCPSrvGlobalPoolName_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,2,1,1),_HpnicfDHCPSrvGlobalPoolName_Type())
hpnicfDHCPSrvGlobalPoolName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolName.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolRowStatus_Type=RowStatus
_HpnicfDHCPSrvGlobalPoolRowStatus_Object=MibTableColumn
hpnicfDHCPSrvGlobalPoolRowStatus=_HpnicfDHCPSrvGlobalPoolRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,2,1,2),_HpnicfDHCPSrvGlobalPoolRowStatus_Type())
hpnicfDHCPSrvGlobalPoolRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolRowStatus.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolConfigTable_Object=MibTable
hpnicfDHCPSrvGlobalPoolConfigTable=_HpnicfDHCPSrvGlobalPoolConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,3))
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolConfigTable.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolConfigEntry_Object=MibTableRow
hpnicfDHCPSrvGlobalPoolConfigEntry=_HpnicfDHCPSrvGlobalPoolConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,3,1))
hpnicfDHCPSrvGlobalPoolConfigEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolConfigEntry.setStatus(_A)
class _HpnicfDHCPSrvGlobalPoolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('null',0),('host',1),('network',2)))
_HpnicfDHCPSrvGlobalPoolType_Type.__name__=_C
_HpnicfDHCPSrvGlobalPoolType_Object=MibTableColumn
hpnicfDHCPSrvGlobalPoolType=_HpnicfDHCPSrvGlobalPoolType_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,3,1,1),_HpnicfDHCPSrvGlobalPoolType_Type())
hpnicfDHCPSrvGlobalPoolType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolType.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolNetwork_Type=IpAddress
_HpnicfDHCPSrvGlobalPoolNetwork_Object=MibTableColumn
hpnicfDHCPSrvGlobalPoolNetwork=_HpnicfDHCPSrvGlobalPoolNetwork_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,3,1,2),_HpnicfDHCPSrvGlobalPoolNetwork_Type())
hpnicfDHCPSrvGlobalPoolNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolNetwork.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolNetworkMask_Type=IpAddress
_HpnicfDHCPSrvGlobalPoolNetworkMask_Object=MibTableColumn
hpnicfDHCPSrvGlobalPoolNetworkMask=_HpnicfDHCPSrvGlobalPoolNetworkMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,3,1,3),_HpnicfDHCPSrvGlobalPoolNetworkMask_Type())
hpnicfDHCPSrvGlobalPoolNetworkMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolNetworkMask.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolHostIPAddr_Type=IpAddress
_HpnicfDHCPSrvGlobalPoolHostIPAddr_Object=MibTableColumn
hpnicfDHCPSrvGlobalPoolHostIPAddr=_HpnicfDHCPSrvGlobalPoolHostIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,3,1,4),_HpnicfDHCPSrvGlobalPoolHostIPAddr_Type())
hpnicfDHCPSrvGlobalPoolHostIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolHostIPAddr.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolHostMask_Type=IpAddress
_HpnicfDHCPSrvGlobalPoolHostMask_Object=MibTableColumn
hpnicfDHCPSrvGlobalPoolHostMask=_HpnicfDHCPSrvGlobalPoolHostMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,3,1,5),_HpnicfDHCPSrvGlobalPoolHostMask_Type())
hpnicfDHCPSrvGlobalPoolHostMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolHostMask.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolHostHAddr_Type=MacAddress
_HpnicfDHCPSrvGlobalPoolHostHAddr_Object=MibTableColumn
hpnicfDHCPSrvGlobalPoolHostHAddr=_HpnicfDHCPSrvGlobalPoolHostHAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,3,1,6),_HpnicfDHCPSrvGlobalPoolHostHAddr_Type())
hpnicfDHCPSrvGlobalPoolHostHAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolHostHAddr.setStatus(_A)
class _HpnicfDHCPSrvGlobalPoolCfgUndoFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('undonetworkip',1),('undohostip',2),('undohosthaddr',3)))
_HpnicfDHCPSrvGlobalPoolCfgUndoFlag_Type.__name__=_C
_HpnicfDHCPSrvGlobalPoolCfgUndoFlag_Object=MibTableColumn
hpnicfDHCPSrvGlobalPoolCfgUndoFlag=_HpnicfDHCPSrvGlobalPoolCfgUndoFlag_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,3,1,7),_HpnicfDHCPSrvGlobalPoolCfgUndoFlag_Type())
hpnicfDHCPSrvGlobalPoolCfgUndoFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolCfgUndoFlag.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolStartAddr_Type=IpAddress
_HpnicfDHCPSrvGlobalPoolStartAddr_Object=MibTableColumn
hpnicfDHCPSrvGlobalPoolStartAddr=_HpnicfDHCPSrvGlobalPoolStartAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,3,1,8),_HpnicfDHCPSrvGlobalPoolStartAddr_Type())
hpnicfDHCPSrvGlobalPoolStartAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolStartAddr.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolEndAddr_Type=IpAddress
_HpnicfDHCPSrvGlobalPoolEndAddr_Object=MibTableColumn
hpnicfDHCPSrvGlobalPoolEndAddr=_HpnicfDHCPSrvGlobalPoolEndAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,3,1,9),_HpnicfDHCPSrvGlobalPoolEndAddr_Type())
hpnicfDHCPSrvGlobalPoolEndAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolEndAddr.setStatus(_A)
class _HpnicfDHCPSrvGlobalPoolAllocObject_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('user',0),('admin',1)))
_HpnicfDHCPSrvGlobalPoolAllocObject_Type.__name__=_C
_HpnicfDHCPSrvGlobalPoolAllocObject_Object=MibTableColumn
hpnicfDHCPSrvGlobalPoolAllocObject=_HpnicfDHCPSrvGlobalPoolAllocObject_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,3,1,10),_HpnicfDHCPSrvGlobalPoolAllocObject_Type())
hpnicfDHCPSrvGlobalPoolAllocObject.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolAllocObject.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolParaTable_Object=MibTable
hpnicfDHCPSrvGlobalPoolParaTable=_HpnicfDHCPSrvGlobalPoolParaTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4))
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolParaTable.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolParaEntry_Object=MibTableRow
hpnicfDHCPSrvGlobalPoolParaEntry=_HpnicfDHCPSrvGlobalPoolParaEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1))
hpnicfDHCPSrvGlobalPoolParaEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolParaEntry.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolLeaseDay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,365))
_HpnicfDHCPSrvGlbPoolLeaseDay_Type.__name__=_C
_HpnicfDHCPSrvGlbPoolLeaseDay_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseDay=_HpnicfDHCPSrvGlbPoolLeaseDay_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,1),_HpnicfDHCPSrvGlbPoolLeaseDay_Type())
hpnicfDHCPSrvGlbPoolLeaseDay.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolLeaseDay.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolLeaseHour_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_HpnicfDHCPSrvGlbPoolLeaseHour_Type.__name__=_C
_HpnicfDHCPSrvGlbPoolLeaseHour_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseHour=_HpnicfDHCPSrvGlbPoolLeaseHour_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,2),_HpnicfDHCPSrvGlbPoolLeaseHour_Type())
hpnicfDHCPSrvGlbPoolLeaseHour.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolLeaseHour.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolLeaseMinute_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_HpnicfDHCPSrvGlbPoolLeaseMinute_Type.__name__=_C
_HpnicfDHCPSrvGlbPoolLeaseMinute_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseMinute=_HpnicfDHCPSrvGlbPoolLeaseMinute_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,3),_HpnicfDHCPSrvGlbPoolLeaseMinute_Type())
hpnicfDHCPSrvGlbPoolLeaseMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolLeaseMinute.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolLeaseUnlimited_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('invalid',0),('unlimited',1)))
_HpnicfDHCPSrvGlbPoolLeaseUnlimited_Type.__name__=_C
_HpnicfDHCPSrvGlbPoolLeaseUnlimited_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseUnlimited=_HpnicfDHCPSrvGlbPoolLeaseUnlimited_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,4),_HpnicfDHCPSrvGlbPoolLeaseUnlimited_Type())
hpnicfDHCPSrvGlbPoolLeaseUnlimited.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolLeaseUnlimited.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDHCPSrvGlbPoolDomainName_Type.__name__=_F
_HpnicfDHCPSrvGlbPoolDomainName_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolDomainName=_HpnicfDHCPSrvGlbPoolDomainName_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,5),_HpnicfDHCPSrvGlbPoolDomainName_Type())
hpnicfDHCPSrvGlbPoolDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolDomainName.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolCliGWIPStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,129))
_HpnicfDHCPSrvGlbPoolCliGWIPStr_Type.__name__=_F
_HpnicfDHCPSrvGlbPoolCliGWIPStr_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolCliGWIPStr=_HpnicfDHCPSrvGlbPoolCliGWIPStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,6),_HpnicfDHCPSrvGlbPoolCliGWIPStr_Type())
hpnicfDHCPSrvGlbPoolCliGWIPStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolCliGWIPStr.setStatus(_A)
_HpnicfDHCPSrvGlbPoolCliGWIPUndo_Type=IpAddress
_HpnicfDHCPSrvGlbPoolCliGWIPUndo_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolCliGWIPUndo=_HpnicfDHCPSrvGlbPoolCliGWIPUndo_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,7),_HpnicfDHCPSrvGlbPoolCliGWIPUndo_Type())
hpnicfDHCPSrvGlbPoolCliGWIPUndo.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolCliGWIPUndo.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolCliDNSIPStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,129))
_HpnicfDHCPSrvGlbPoolCliDNSIPStr_Type.__name__=_F
_HpnicfDHCPSrvGlbPoolCliDNSIPStr_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolCliDNSIPStr=_HpnicfDHCPSrvGlbPoolCliDNSIPStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,8),_HpnicfDHCPSrvGlbPoolCliDNSIPStr_Type())
hpnicfDHCPSrvGlbPoolCliDNSIPStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolCliDNSIPStr.setStatus(_A)
_HpnicfDHCPSrvGlbPoolCliDNSIPUndo_Type=IpAddress
_HpnicfDHCPSrvGlbPoolCliDNSIPUndo_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolCliDNSIPUndo=_HpnicfDHCPSrvGlbPoolCliDNSIPUndo_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,9),_HpnicfDHCPSrvGlbPoolCliDNSIPUndo_Type())
hpnicfDHCPSrvGlbPoolCliDNSIPUndo.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolCliDNSIPUndo.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolCliNetbiosType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*(('null',0),('bnode',1),('pnode',2),('mnode',4),('hnode',8)))
_HpnicfDHCPSrvGlbPoolCliNetbiosType_Type.__name__=_C
_HpnicfDHCPSrvGlbPoolCliNetbiosType_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolCliNetbiosType=_HpnicfDHCPSrvGlbPoolCliNetbiosType_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,10),_HpnicfDHCPSrvGlbPoolCliNetbiosType_Type())
hpnicfDHCPSrvGlbPoolCliNetbiosType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolCliNetbiosType.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolCliNbnsIPStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,129))
_HpnicfDHCPSrvGlbPoolCliNbnsIPStr_Type.__name__=_F
_HpnicfDHCPSrvGlbPoolCliNbnsIPStr_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolCliNbnsIPStr=_HpnicfDHCPSrvGlbPoolCliNbnsIPStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,11),_HpnicfDHCPSrvGlbPoolCliNbnsIPStr_Type())
hpnicfDHCPSrvGlbPoolCliNbnsIPStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolCliNbnsIPStr.setStatus(_A)
_HpnicfDHCPSrvGlbPoolCliNbnsIPUndo_Type=IpAddress
_HpnicfDHCPSrvGlbPoolCliNbnsIPUndo_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolCliNbnsIPUndo=_HpnicfDHCPSrvGlbPoolCliNbnsIPUndo_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,12),_HpnicfDHCPSrvGlbPoolCliNbnsIPUndo_Type())
hpnicfDHCPSrvGlbPoolCliNbnsIPUndo.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolCliNbnsIPUndo.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolParaUndoFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('undoDomain',1),('undoLease',2),('undoGateway',3),('undoDns',4),('undoNbns',5),('undoNbType',6)))
_HpnicfDHCPSrvGlbPoolParaUndoFlag_Type.__name__=_C
_HpnicfDHCPSrvGlbPoolParaUndoFlag_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolParaUndoFlag=_HpnicfDHCPSrvGlbPoolParaUndoFlag_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,13),_HpnicfDHCPSrvGlbPoolParaUndoFlag_Type())
hpnicfDHCPSrvGlbPoolParaUndoFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolParaUndoFlag.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolIPInUseReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_HpnicfDHCPSrvGlbPoolIPInUseReset_Type.__name__=_C
_HpnicfDHCPSrvGlbPoolIPInUseReset_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolIPInUseReset=_HpnicfDHCPSrvGlbPoolIPInUseReset_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,14),_HpnicfDHCPSrvGlbPoolIPInUseReset_Type())
hpnicfDHCPSrvGlbPoolIPInUseReset.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolIPInUseReset.setStatus(_A)
_HpnicfDHCPSrvGlbPoolLeaseTime_Type=TimeTicks
_HpnicfDHCPSrvGlbPoolLeaseTime_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseTime=_HpnicfDHCPSrvGlbPoolLeaseTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,15),_HpnicfDHCPSrvGlbPoolLeaseTime_Type())
hpnicfDHCPSrvGlbPoolLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolLeaseTime.setStatus(_A)
_HpnicfDHCPSrvGlbPoolPrimaryDNSIP_Type=IpAddress
_HpnicfDHCPSrvGlbPoolPrimaryDNSIP_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolPrimaryDNSIP=_HpnicfDHCPSrvGlbPoolPrimaryDNSIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,16),_HpnicfDHCPSrvGlbPoolPrimaryDNSIP_Type())
hpnicfDHCPSrvGlbPoolPrimaryDNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolPrimaryDNSIP.setStatus(_A)
_HpnicfDHCPSrvGlbPoolSecondaryDNSIP_Type=IpAddress
_HpnicfDHCPSrvGlbPoolSecondaryDNSIP_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolSecondaryDNSIP=_HpnicfDHCPSrvGlbPoolSecondaryDNSIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,17),_HpnicfDHCPSrvGlbPoolSecondaryDNSIP_Type())
hpnicfDHCPSrvGlbPoolSecondaryDNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolSecondaryDNSIP.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolLeaseSecond_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_HpnicfDHCPSrvGlbPoolLeaseSecond_Type.__name__=_C
_HpnicfDHCPSrvGlbPoolLeaseSecond_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseSecond=_HpnicfDHCPSrvGlbPoolLeaseSecond_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,18),_HpnicfDHCPSrvGlbPoolLeaseSecond_Type())
hpnicfDHCPSrvGlbPoolLeaseSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolLeaseSecond.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolLeaseTimeSec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,31622399))
_HpnicfDHCPSrvGlbPoolLeaseTimeSec_Type.__name__=_C
_HpnicfDHCPSrvGlbPoolLeaseTimeSec_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolLeaseTimeSec=_HpnicfDHCPSrvGlbPoolLeaseTimeSec_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,19),_HpnicfDHCPSrvGlbPoolLeaseTimeSec_Type())
hpnicfDHCPSrvGlbPoolLeaseTimeSec.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolLeaseTimeSec.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolLeaseTimeSec.setUnits('seconds')
_HpnicfDHCPSrvGlbPoolCliGWIPAddr_Type=IpAddress
_HpnicfDHCPSrvGlbPoolCliGWIPAddr_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolCliGWIPAddr=_HpnicfDHCPSrvGlbPoolCliGWIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,4,1,20),_HpnicfDHCPSrvGlbPoolCliGWIPAddr_Type())
hpnicfDHCPSrvGlbPoolCliGWIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolCliGWIPAddr.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolOptionTable_Object=MibTable
hpnicfDHCPSrvGlobalPoolOptionTable=_HpnicfDHCPSrvGlobalPoolOptionTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,5))
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolOptionTable.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolOptionEntry_Object=MibTableRow
hpnicfDHCPSrvGlobalPoolOptionEntry=_HpnicfDHCPSrvGlobalPoolOptionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,5,1))
hpnicfDHCPSrvGlobalPoolOptionEntry.setIndexNames((0,_D,_H),(0,_D,_M))
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolOptionEntry.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolOptCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_HpnicfDHCPSrvGlbPoolOptCode_Type.__name__=_C
_HpnicfDHCPSrvGlbPoolOptCode_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolOptCode=_HpnicfDHCPSrvGlbPoolOptCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,5,1,1),_HpnicfDHCPSrvGlbPoolOptCode_Type())
hpnicfDHCPSrvGlbPoolOptCode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolOptCode.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolOptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ascii',1),('hex',2),('ip',3)))
_HpnicfDHCPSrvGlbPoolOptType_Type.__name__=_C
_HpnicfDHCPSrvGlbPoolOptType_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolOptType=_HpnicfDHCPSrvGlbPoolOptType_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,5,1,2),_HpnicfDHCPSrvGlbPoolOptType_Type())
hpnicfDHCPSrvGlbPoolOptType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolOptType.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolOptAscii_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpnicfDHCPSrvGlbPoolOptAscii_Type.__name__=_F
_HpnicfDHCPSrvGlbPoolOptAscii_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolOptAscii=_HpnicfDHCPSrvGlbPoolOptAscii_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,5,1,3),_HpnicfDHCPSrvGlbPoolOptAscii_Type())
hpnicfDHCPSrvGlbPoolOptAscii.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolOptAscii.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolOptHexString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,573))
_HpnicfDHCPSrvGlbPoolOptHexString_Type.__name__=_F
_HpnicfDHCPSrvGlbPoolOptHexString_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolOptHexString=_HpnicfDHCPSrvGlbPoolOptHexString_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,5,1,4),_HpnicfDHCPSrvGlbPoolOptHexString_Type())
hpnicfDHCPSrvGlbPoolOptHexString.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolOptHexString.setStatus(_A)
class _HpnicfDHCPSrvGlbPoolOptIPString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,129))
_HpnicfDHCPSrvGlbPoolOptIPString_Type.__name__=_F
_HpnicfDHCPSrvGlbPoolOptIPString_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolOptIPString=_HpnicfDHCPSrvGlbPoolOptIPString_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,5,1,5),_HpnicfDHCPSrvGlbPoolOptIPString_Type())
hpnicfDHCPSrvGlbPoolOptIPString.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolOptIPString.setStatus(_A)
_HpnicfDHCPSrvGlbPoolOptRowStatus_Type=RowStatus
_HpnicfDHCPSrvGlbPoolOptRowStatus_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolOptRowStatus=_HpnicfDHCPSrvGlbPoolOptRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,5,1,6),_HpnicfDHCPSrvGlbPoolOptRowStatus_Type())
hpnicfDHCPSrvGlbPoolOptRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolOptRowStatus.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolStatTable_Object=MibTable
hpnicfDHCPSrvGlobalPoolStatTable=_HpnicfDHCPSrvGlobalPoolStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,6))
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolStatTable.setStatus(_A)
_HpnicfDHCPSrvGlobalPoolStatEntry_Object=MibTableRow
hpnicfDHCPSrvGlobalPoolStatEntry=_HpnicfDHCPSrvGlobalPoolStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,6,1))
hpnicfDHCPSrvGlobalPoolStatEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hpnicfDHCPSrvGlobalPoolStatEntry.setStatus(_A)
_HpnicfDHCPSrvGlbPoolIPPoolUsage_Type=Integer32
_HpnicfDHCPSrvGlbPoolIPPoolUsage_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolIPPoolUsage=_HpnicfDHCPSrvGlbPoolIPPoolUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,6,1,1),_HpnicfDHCPSrvGlbPoolIPPoolUsage_Type())
hpnicfDHCPSrvGlbPoolIPPoolUsage.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolIPPoolUsage.setStatus(_A)
_HpnicfDHCPSrvGlbPoolReqTimes_Type=Counter32
_HpnicfDHCPSrvGlbPoolReqTimes_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolReqTimes=_HpnicfDHCPSrvGlbPoolReqTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,6,1,2),_HpnicfDHCPSrvGlbPoolReqTimes_Type())
hpnicfDHCPSrvGlbPoolReqTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolReqTimes.setStatus(_A)
_HpnicfDHCPSrvGlbPoolSuccessTimes_Type=Counter32
_HpnicfDHCPSrvGlbPoolSuccessTimes_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolSuccessTimes=_HpnicfDHCPSrvGlbPoolSuccessTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,6,1,3),_HpnicfDHCPSrvGlbPoolSuccessTimes_Type())
hpnicfDHCPSrvGlbPoolSuccessTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolSuccessTimes.setStatus(_A)
_HpnicfDHCPSrvGlbPoolDiscoverTimes_Type=Counter32
_HpnicfDHCPSrvGlbPoolDiscoverTimes_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolDiscoverTimes=_HpnicfDHCPSrvGlbPoolDiscoverTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,6,1,4),_HpnicfDHCPSrvGlbPoolDiscoverTimes_Type())
hpnicfDHCPSrvGlbPoolDiscoverTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolDiscoverTimes.setStatus(_A)
_HpnicfDHCPSrvGlbPoolOfferTimes_Type=Counter32
_HpnicfDHCPSrvGlbPoolOfferTimes_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolOfferTimes=_HpnicfDHCPSrvGlbPoolOfferTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,6,1,5),_HpnicfDHCPSrvGlbPoolOfferTimes_Type())
hpnicfDHCPSrvGlbPoolOfferTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolOfferTimes.setStatus(_A)
_HpnicfDHCPSrvGlbPoolACKTimes_Type=Counter32
_HpnicfDHCPSrvGlbPoolACKTimes_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolACKTimes=_HpnicfDHCPSrvGlbPoolACKTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,6,1,6),_HpnicfDHCPSrvGlbPoolACKTimes_Type())
hpnicfDHCPSrvGlbPoolACKTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolACKTimes.setStatus(_A)
_HpnicfDHCPSrvGlbPoolTotalIpNum_Type=Counter32
_HpnicfDHCPSrvGlbPoolTotalIpNum_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolTotalIpNum=_HpnicfDHCPSrvGlbPoolTotalIpNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,6,1,7),_HpnicfDHCPSrvGlbPoolTotalIpNum_Type())
hpnicfDHCPSrvGlbPoolTotalIpNum.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolTotalIpNum.setStatus(_A)
_HpnicfDHCPSrvGlbPoolInUsedIpNum_Type=Counter32
_HpnicfDHCPSrvGlbPoolInUsedIpNum_Object=MibTableColumn
hpnicfDHCPSrvGlbPoolInUsedIpNum=_HpnicfDHCPSrvGlbPoolInUsedIpNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,6,1,8),_HpnicfDHCPSrvGlbPoolInUsedIpNum_Type())
hpnicfDHCPSrvGlbPoolInUsedIpNum.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSrvGlbPoolInUsedIpNum.setStatus(_A)
_HpnicfDHCPSvrOptionGroupTable_Object=MibTable
hpnicfDHCPSvrOptionGroupTable=_HpnicfDHCPSvrOptionGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,7))
if mibBuilder.loadTexts:hpnicfDHCPSvrOptionGroupTable.setStatus(_A)
_HpnicfDHCPSvrOptionGroupEntry_Object=MibTableRow
hpnicfDHCPSvrOptionGroupEntry=_HpnicfDHCPSvrOptionGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,7,1))
hpnicfDHCPSvrOptionGroupEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnicfDHCPSvrOptionGroupEntry.setStatus(_A)
class _HpnicfDHCPSvrOptionGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfDHCPSvrOptionGroupIndex_Type.__name__=_C
_HpnicfDHCPSvrOptionGroupIndex_Object=MibTableColumn
hpnicfDHCPSvrOptionGroupIndex=_HpnicfDHCPSvrOptionGroupIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,7,1,1),_HpnicfDHCPSvrOptionGroupIndex_Type())
hpnicfDHCPSvrOptionGroupIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSvrOptionGroupIndex.setStatus(_A)
_HpnicfDHCPSvrOptionGroupRowstatus_Type=RowStatus
_HpnicfDHCPSvrOptionGroupRowstatus_Object=MibTableColumn
hpnicfDHCPSvrOptionGroupRowstatus=_HpnicfDHCPSvrOptionGroupRowstatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,7,1,2),_HpnicfDHCPSvrOptionGroupRowstatus_Type())
hpnicfDHCPSvrOptionGroupRowstatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSvrOptionGroupRowstatus.setStatus(_A)
_HpnicfDHCPSvrOptionTable_Object=MibTable
hpnicfDHCPSvrOptionTable=_HpnicfDHCPSvrOptionTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,8))
if mibBuilder.loadTexts:hpnicfDHCPSvrOptionTable.setStatus(_A)
_HpnicfDHCPSvrOptionEntry_Object=MibTableRow
hpnicfDHCPSvrOptionEntry=_HpnicfDHCPSvrOptionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,8,1))
hpnicfDHCPSvrOptionEntry.setIndexNames((0,_D,_J),(0,_D,_N))
if mibBuilder.loadTexts:hpnicfDHCPSvrOptionEntry.setStatus(_A)
class _HpnicfDHCPSvrOptionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_HpnicfDHCPSvrOptionCode_Type.__name__=_C
_HpnicfDHCPSvrOptionCode_Object=MibTableColumn
hpnicfDHCPSvrOptionCode=_HpnicfDHCPSvrOptionCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,8,1,1),_HpnicfDHCPSvrOptionCode_Type())
hpnicfDHCPSvrOptionCode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSvrOptionCode.setStatus(_A)
class _HpnicfDHCPSvrOptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ascii',1),('hex',2),('ip',3)))
_HpnicfDHCPSvrOptionType_Type.__name__=_C
_HpnicfDHCPSvrOptionType_Object=MibTableColumn
hpnicfDHCPSvrOptionType=_HpnicfDHCPSvrOptionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,8,1,2),_HpnicfDHCPSvrOptionType_Type())
hpnicfDHCPSvrOptionType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSvrOptionType.setStatus(_A)
class _HpnicfDHCPSvrOptionAsciiString_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDHCPSvrOptionAsciiString_Type.__name__=_F
_HpnicfDHCPSvrOptionAsciiString_Object=MibTableColumn
hpnicfDHCPSvrOptionAsciiString=_HpnicfDHCPSvrOptionAsciiString_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,8,1,3),_HpnicfDHCPSvrOptionAsciiString_Type())
hpnicfDHCPSvrOptionAsciiString.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSvrOptionAsciiString.setStatus(_A)
class _HpnicfDHCPSvrOptionHexString_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,573))
_HpnicfDHCPSvrOptionHexString_Type.__name__=_F
_HpnicfDHCPSvrOptionHexString_Object=MibTableColumn
hpnicfDHCPSvrOptionHexString=_HpnicfDHCPSvrOptionHexString_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,8,1,4),_HpnicfDHCPSvrOptionHexString_Type())
hpnicfDHCPSvrOptionHexString.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSvrOptionHexString.setStatus(_A)
class _HpnicfDHCPSvrOptionIPString_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,129))
_HpnicfDHCPSvrOptionIPString_Type.__name__=_F
_HpnicfDHCPSvrOptionIPString_Object=MibTableColumn
hpnicfDHCPSvrOptionIPString=_HpnicfDHCPSvrOptionIPString_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,8,1,5),_HpnicfDHCPSvrOptionIPString_Type())
hpnicfDHCPSvrOptionIPString.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSvrOptionIPString.setStatus(_A)
_HpnicfDHCPSvrOptionRowstatus_Type=RowStatus
_HpnicfDHCPSvrOptionRowstatus_Object=MibTableColumn
hpnicfDHCPSvrOptionRowstatus=_HpnicfDHCPSvrOptionRowstatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,8,1,6),_HpnicfDHCPSvrOptionRowstatus_Type())
hpnicfDHCPSvrOptionRowstatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSvrOptionRowstatus.setStatus(_A)
_HpnicfDHCPSvrVerifyMacTable_Object=MibTable
hpnicfDHCPSvrVerifyMacTable=_HpnicfDHCPSvrVerifyMacTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,9))
if mibBuilder.loadTexts:hpnicfDHCPSvrVerifyMacTable.setStatus(_A)
_HpnicfDHCPSvrVerifyMacEntry_Object=MibTableRow
hpnicfDHCPSvrVerifyMacEntry=_HpnicfDHCPSvrVerifyMacEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,9,1))
hpnicfDHCPSvrVerifyMacEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hpnicfDHCPSvrVerifyMacEntry.setStatus(_A)
class _HpnicfDHCPSvrVerifyMacSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfDHCPSvrVerifyMacSwitch_Type.__name__=_C
_HpnicfDHCPSvrVerifyMacSwitch_Object=MibTableColumn
hpnicfDHCPSvrVerifyMacSwitch=_HpnicfDHCPSvrVerifyMacSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,9,1,1),_HpnicfDHCPSvrVerifyMacSwitch_Type())
hpnicfDHCPSvrVerifyMacSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSvrVerifyMacSwitch.setStatus(_A)
_HpnicfDHCPSvrPoolMacTable_Object=MibTable
hpnicfDHCPSvrPoolMacTable=_HpnicfDHCPSvrPoolMacTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,10))
if mibBuilder.loadTexts:hpnicfDHCPSvrPoolMacTable.setStatus(_A)
_HpnicfDHCPSvrPoolMacEntry_Object=MibTableRow
hpnicfDHCPSvrPoolMacEntry=_HpnicfDHCPSvrPoolMacEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,10,1))
hpnicfDHCPSvrPoolMacEntry.setIndexNames((0,_D,_H),(0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:hpnicfDHCPSvrPoolMacEntry.setStatus(_A)
_HpnicfDHCPSvrPoolMac_Type=MacAddress
_HpnicfDHCPSvrPoolMac_Object=MibTableColumn
hpnicfDHCPSvrPoolMac=_HpnicfDHCPSvrPoolMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,10,1,1),_HpnicfDHCPSvrPoolMac_Type())
hpnicfDHCPSvrPoolMac.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSvrPoolMac.setStatus(_A)
_HpnicfDHCPSvrPoolMacMask_Type=MacAddress
_HpnicfDHCPSvrPoolMacMask_Object=MibTableColumn
hpnicfDHCPSvrPoolMacMask=_HpnicfDHCPSvrPoolMacMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,10,1,2),_HpnicfDHCPSvrPoolMacMask_Type())
hpnicfDHCPSvrPoolMacMask.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDHCPSvrPoolMacMask.setStatus(_A)
class _HpnicfDHCPSvrPoolMacOptIndex_Type(Integer32):defaultValue=0
_HpnicfDHCPSvrPoolMacOptIndex_Type.__name__=_C
_HpnicfDHCPSvrPoolMacOptIndex_Object=MibTableColumn
hpnicfDHCPSvrPoolMacOptIndex=_HpnicfDHCPSvrPoolMacOptIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,10,1,3),_HpnicfDHCPSvrPoolMacOptIndex_Type())
hpnicfDHCPSvrPoolMacOptIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPSvrPoolMacOptIndex.setStatus(_A)
_HpnicfDHCPSvrPoolMacRowstatus_Type=RowStatus
_HpnicfDHCPSvrPoolMacRowstatus_Object=MibTableColumn
hpnicfDHCPSvrPoolMacRowstatus=_HpnicfDHCPSvrPoolMacRowstatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,2,10,1,4),_HpnicfDHCPSvrPoolMacRowstatus_Type())
hpnicfDHCPSvrPoolMacRowstatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDHCPSvrPoolMacRowstatus.setStatus(_A)
_HpnicfDHCPServerTraps_ObjectIdentity=ObjectIdentity
hpnicfDHCPServerTraps=_HpnicfDHCPServerTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,101,3))
_HpnicfDHCPServerTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfDHCPServerTrapPrefix=_HpnicfDHCPServerTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,101,3,0))
_HpnicfDHCPServerTrapObjects_ObjectIdentity=ObjectIdentity
hpnicfDHCPServerTrapObjects=_HpnicfDHCPServerTrapObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,101,3,1))
_HpnicfDHCPServerFirstTrapTime_Type=TimeTicks
_HpnicfDHCPServerFirstTrapTime_Object=MibScalar
hpnicfDHCPServerFirstTrapTime=_HpnicfDHCPServerFirstTrapTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,101,3,1,1),_HpnicfDHCPServerFirstTrapTime_Type())
hpnicfDHCPServerFirstTrapTime.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfDHCPServerFirstTrapTime.setStatus(_A)
hpnicfDHCPServerAddrExhaust=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,101,3,0,1))
hpnicfDHCPServerAddrExhaust.setObjects(*((_D,_I),(_D,_K)))
if mibBuilder.loadTexts:hpnicfDHCPServerAddrExhaust.setStatus(_A)
hpnicfDHCPServerAddrExhaustRecover=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,101,3,0,2))
hpnicfDHCPServerAddrExhaustRecover.setObjects(*((_D,_I),(_D,_K)))
if mibBuilder.loadTexts:hpnicfDHCPServerAddrExhaustRecover.setStatus(_A)
hpnicfDHCPServerAvgIpUsageOverflow=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,101,3,0,3))
hpnicfDHCPServerAvgIpUsageOverflow.setObjects((_D,_I))
if mibBuilder.loadTexts:hpnicfDHCPServerAvgIpUsageOverflow.setStatus(_A)
hpnicfDHCPServerMaxIpUsageOverflow=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,101,3,0,4))
hpnicfDHCPServerMaxIpUsageOverflow.setObjects((_D,_I))
if mibBuilder.loadTexts:hpnicfDHCPServerMaxIpUsageOverflow.setStatus(_A)
hpnicfDHCPServerAllocateOverflow=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,101,3,0,5))
if mibBuilder.loadTexts:hpnicfDHCPServerAllocateOverflow.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfDHCPServer':hpnicfDHCPServer,'hpnicfDHCPServerObjects':hpnicfDHCPServerObjects,'hpnicfDHCPServerIPPoolUsage':hpnicfDHCPServerIPPoolUsage,'hpnicfDHCPServerReqTimes':hpnicfDHCPServerReqTimes,'hpnicfDHCPServerReqSuccessTimes':hpnicfDHCPServerReqSuccessTimes,'hpnicfDHCPServerAvgIpUseThreshold':hpnicfDHCPServerAvgIpUseThreshold,'hpnicfDHCPServerMaxIpUseThreshold':hpnicfDHCPServerMaxIpUseThreshold,'hpnicfDHCPServerAllocateThreshold':hpnicfDHCPServerAllocateThreshold,'hpnicfDHCPServerTables':hpnicfDHCPServerTables,_I:hpnicfDHCPServerPoolName,'hpnicfDHCPSrvGlobalPoolTable':hpnicfDHCPSrvGlobalPoolTable,'hpnicfDHCPSrvGlobalPoolEntry':hpnicfDHCPSrvGlobalPoolEntry,_H:hpnicfDHCPSrvGlobalPoolName,'hpnicfDHCPSrvGlobalPoolRowStatus':hpnicfDHCPSrvGlobalPoolRowStatus,'hpnicfDHCPSrvGlobalPoolConfigTable':hpnicfDHCPSrvGlobalPoolConfigTable,'hpnicfDHCPSrvGlobalPoolConfigEntry':hpnicfDHCPSrvGlobalPoolConfigEntry,'hpnicfDHCPSrvGlobalPoolType':hpnicfDHCPSrvGlobalPoolType,'hpnicfDHCPSrvGlobalPoolNetwork':hpnicfDHCPSrvGlobalPoolNetwork,'hpnicfDHCPSrvGlobalPoolNetworkMask':hpnicfDHCPSrvGlobalPoolNetworkMask,'hpnicfDHCPSrvGlobalPoolHostIPAddr':hpnicfDHCPSrvGlobalPoolHostIPAddr,'hpnicfDHCPSrvGlobalPoolHostMask':hpnicfDHCPSrvGlobalPoolHostMask,'hpnicfDHCPSrvGlobalPoolHostHAddr':hpnicfDHCPSrvGlobalPoolHostHAddr,'hpnicfDHCPSrvGlobalPoolCfgUndoFlag':hpnicfDHCPSrvGlobalPoolCfgUndoFlag,'hpnicfDHCPSrvGlobalPoolStartAddr':hpnicfDHCPSrvGlobalPoolStartAddr,'hpnicfDHCPSrvGlobalPoolEndAddr':hpnicfDHCPSrvGlobalPoolEndAddr,'hpnicfDHCPSrvGlobalPoolAllocObject':hpnicfDHCPSrvGlobalPoolAllocObject,'hpnicfDHCPSrvGlobalPoolParaTable':hpnicfDHCPSrvGlobalPoolParaTable,'hpnicfDHCPSrvGlobalPoolParaEntry':hpnicfDHCPSrvGlobalPoolParaEntry,'hpnicfDHCPSrvGlbPoolLeaseDay':hpnicfDHCPSrvGlbPoolLeaseDay,'hpnicfDHCPSrvGlbPoolLeaseHour':hpnicfDHCPSrvGlbPoolLeaseHour,'hpnicfDHCPSrvGlbPoolLeaseMinute':hpnicfDHCPSrvGlbPoolLeaseMinute,'hpnicfDHCPSrvGlbPoolLeaseUnlimited':hpnicfDHCPSrvGlbPoolLeaseUnlimited,'hpnicfDHCPSrvGlbPoolDomainName':hpnicfDHCPSrvGlbPoolDomainName,'hpnicfDHCPSrvGlbPoolCliGWIPStr':hpnicfDHCPSrvGlbPoolCliGWIPStr,'hpnicfDHCPSrvGlbPoolCliGWIPUndo':hpnicfDHCPSrvGlbPoolCliGWIPUndo,'hpnicfDHCPSrvGlbPoolCliDNSIPStr':hpnicfDHCPSrvGlbPoolCliDNSIPStr,'hpnicfDHCPSrvGlbPoolCliDNSIPUndo':hpnicfDHCPSrvGlbPoolCliDNSIPUndo,'hpnicfDHCPSrvGlbPoolCliNetbiosType':hpnicfDHCPSrvGlbPoolCliNetbiosType,'hpnicfDHCPSrvGlbPoolCliNbnsIPStr':hpnicfDHCPSrvGlbPoolCliNbnsIPStr,'hpnicfDHCPSrvGlbPoolCliNbnsIPUndo':hpnicfDHCPSrvGlbPoolCliNbnsIPUndo,'hpnicfDHCPSrvGlbPoolParaUndoFlag':hpnicfDHCPSrvGlbPoolParaUndoFlag,'hpnicfDHCPSrvGlbPoolIPInUseReset':hpnicfDHCPSrvGlbPoolIPInUseReset,'hpnicfDHCPSrvGlbPoolLeaseTime':hpnicfDHCPSrvGlbPoolLeaseTime,'hpnicfDHCPSrvGlbPoolPrimaryDNSIP':hpnicfDHCPSrvGlbPoolPrimaryDNSIP,'hpnicfDHCPSrvGlbPoolSecondaryDNSIP':hpnicfDHCPSrvGlbPoolSecondaryDNSIP,'hpnicfDHCPSrvGlbPoolLeaseSecond':hpnicfDHCPSrvGlbPoolLeaseSecond,'hpnicfDHCPSrvGlbPoolLeaseTimeSec':hpnicfDHCPSrvGlbPoolLeaseTimeSec,'hpnicfDHCPSrvGlbPoolCliGWIPAddr':hpnicfDHCPSrvGlbPoolCliGWIPAddr,'hpnicfDHCPSrvGlobalPoolOptionTable':hpnicfDHCPSrvGlobalPoolOptionTable,'hpnicfDHCPSrvGlobalPoolOptionEntry':hpnicfDHCPSrvGlobalPoolOptionEntry,_M:hpnicfDHCPSrvGlbPoolOptCode,'hpnicfDHCPSrvGlbPoolOptType':hpnicfDHCPSrvGlbPoolOptType,'hpnicfDHCPSrvGlbPoolOptAscii':hpnicfDHCPSrvGlbPoolOptAscii,'hpnicfDHCPSrvGlbPoolOptHexString':hpnicfDHCPSrvGlbPoolOptHexString,'hpnicfDHCPSrvGlbPoolOptIPString':hpnicfDHCPSrvGlbPoolOptIPString,'hpnicfDHCPSrvGlbPoolOptRowStatus':hpnicfDHCPSrvGlbPoolOptRowStatus,'hpnicfDHCPSrvGlobalPoolStatTable':hpnicfDHCPSrvGlobalPoolStatTable,'hpnicfDHCPSrvGlobalPoolStatEntry':hpnicfDHCPSrvGlobalPoolStatEntry,'hpnicfDHCPSrvGlbPoolIPPoolUsage':hpnicfDHCPSrvGlbPoolIPPoolUsage,'hpnicfDHCPSrvGlbPoolReqTimes':hpnicfDHCPSrvGlbPoolReqTimes,'hpnicfDHCPSrvGlbPoolSuccessTimes':hpnicfDHCPSrvGlbPoolSuccessTimes,'hpnicfDHCPSrvGlbPoolDiscoverTimes':hpnicfDHCPSrvGlbPoolDiscoverTimes,'hpnicfDHCPSrvGlbPoolOfferTimes':hpnicfDHCPSrvGlbPoolOfferTimes,'hpnicfDHCPSrvGlbPoolACKTimes':hpnicfDHCPSrvGlbPoolACKTimes,'hpnicfDHCPSrvGlbPoolTotalIpNum':hpnicfDHCPSrvGlbPoolTotalIpNum,'hpnicfDHCPSrvGlbPoolInUsedIpNum':hpnicfDHCPSrvGlbPoolInUsedIpNum,'hpnicfDHCPSvrOptionGroupTable':hpnicfDHCPSvrOptionGroupTable,'hpnicfDHCPSvrOptionGroupEntry':hpnicfDHCPSvrOptionGroupEntry,_J:hpnicfDHCPSvrOptionGroupIndex,'hpnicfDHCPSvrOptionGroupRowstatus':hpnicfDHCPSvrOptionGroupRowstatus,'hpnicfDHCPSvrOptionTable':hpnicfDHCPSvrOptionTable,'hpnicfDHCPSvrOptionEntry':hpnicfDHCPSvrOptionEntry,_N:hpnicfDHCPSvrOptionCode,'hpnicfDHCPSvrOptionType':hpnicfDHCPSvrOptionType,'hpnicfDHCPSvrOptionAsciiString':hpnicfDHCPSvrOptionAsciiString,'hpnicfDHCPSvrOptionHexString':hpnicfDHCPSvrOptionHexString,'hpnicfDHCPSvrOptionIPString':hpnicfDHCPSvrOptionIPString,'hpnicfDHCPSvrOptionRowstatus':hpnicfDHCPSvrOptionRowstatus,'hpnicfDHCPSvrVerifyMacTable':hpnicfDHCPSvrVerifyMacTable,'hpnicfDHCPSvrVerifyMacEntry':hpnicfDHCPSvrVerifyMacEntry,'hpnicfDHCPSvrVerifyMacSwitch':hpnicfDHCPSvrVerifyMacSwitch,'hpnicfDHCPSvrPoolMacTable':hpnicfDHCPSvrPoolMacTable,'hpnicfDHCPSvrPoolMacEntry':hpnicfDHCPSvrPoolMacEntry,_O:hpnicfDHCPSvrPoolMac,_P:hpnicfDHCPSvrPoolMacMask,'hpnicfDHCPSvrPoolMacOptIndex':hpnicfDHCPSvrPoolMacOptIndex,'hpnicfDHCPSvrPoolMacRowstatus':hpnicfDHCPSvrPoolMacRowstatus,'hpnicfDHCPServerTraps':hpnicfDHCPServerTraps,'hpnicfDHCPServerTrapPrefix':hpnicfDHCPServerTrapPrefix,'hpnicfDHCPServerAddrExhaust':hpnicfDHCPServerAddrExhaust,'hpnicfDHCPServerAddrExhaustRecover':hpnicfDHCPServerAddrExhaustRecover,'hpnicfDHCPServerAvgIpUsageOverflow':hpnicfDHCPServerAvgIpUsageOverflow,'hpnicfDHCPServerMaxIpUsageOverflow':hpnicfDHCPServerMaxIpUsageOverflow,'hpnicfDHCPServerAllocateOverflow':hpnicfDHCPServerAllocateOverflow,'hpnicfDHCPServerTrapObjects':hpnicfDHCPServerTrapObjects,_K:hpnicfDHCPServerFirstTrapTime})