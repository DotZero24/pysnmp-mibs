_P='h3cDHCPSvrPoolMacMask'
_O='h3cDHCPSvrPoolMac'
_N='h3cDHCPSvrOptionCode'
_M='h3cDHCPSrvGlbPoolOptCode'
_L='accessible-for-notify'
_K='h3cDHCPServerFirstTrapTime'
_J='h3cDHCPSvrOptionGroupIndex'
_I='h3cDHCPServerPoolName'
_H='h3cDHCPSrvGlobalPoolName'
_G='read-create'
_F='OctetString'
_E='read-only'
_D='H3C-DHCP-SERVER-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
h3cDHCPServer=ModuleIdentity((1,3,6,1,4,1,2011,10,2,101))
if mibBuilder.loadTexts:h3cDHCPServer.setRevisions(('2009-05-06 00:00',))
_H3cDHCPServerObjects_ObjectIdentity=ObjectIdentity
h3cDHCPServerObjects=_H3cDHCPServerObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,101,1))
_H3cDHCPServerIPPoolUsage_Type=Integer32
_H3cDHCPServerIPPoolUsage_Object=MibScalar
h3cDHCPServerIPPoolUsage=_H3cDHCPServerIPPoolUsage_Object((1,3,6,1,4,1,2011,10,2,101,1,1),_H3cDHCPServerIPPoolUsage_Type())
h3cDHCPServerIPPoolUsage.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPServerIPPoolUsage.setStatus(_A)
_H3cDHCPServerReqTimes_Type=Counter32
_H3cDHCPServerReqTimes_Object=MibScalar
h3cDHCPServerReqTimes=_H3cDHCPServerReqTimes_Object((1,3,6,1,4,1,2011,10,2,101,1,2),_H3cDHCPServerReqTimes_Type())
h3cDHCPServerReqTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPServerReqTimes.setStatus(_A)
_H3cDHCPServerReqSuccessTimes_Type=Counter32
_H3cDHCPServerReqSuccessTimes_Object=MibScalar
h3cDHCPServerReqSuccessTimes=_H3cDHCPServerReqSuccessTimes_Object((1,3,6,1,4,1,2011,10,2,101,1,3),_H3cDHCPServerReqSuccessTimes_Type())
h3cDHCPServerReqSuccessTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPServerReqSuccessTimes.setStatus(_A)
class _H3cDHCPServerAvgIpUseThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDHCPServerAvgIpUseThreshold_Type.__name__=_C
_H3cDHCPServerAvgIpUseThreshold_Object=MibScalar
h3cDHCPServerAvgIpUseThreshold=_H3cDHCPServerAvgIpUseThreshold_Object((1,3,6,1,4,1,2011,10,2,101,1,4),_H3cDHCPServerAvgIpUseThreshold_Type())
h3cDHCPServerAvgIpUseThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPServerAvgIpUseThreshold.setStatus(_A)
class _H3cDHCPServerMaxIpUseThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDHCPServerMaxIpUseThreshold_Type.__name__=_C
_H3cDHCPServerMaxIpUseThreshold_Object=MibScalar
h3cDHCPServerMaxIpUseThreshold=_H3cDHCPServerMaxIpUseThreshold_Object((1,3,6,1,4,1,2011,10,2,101,1,5),_H3cDHCPServerMaxIpUseThreshold_Type())
h3cDHCPServerMaxIpUseThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPServerMaxIpUseThreshold.setStatus(_A)
class _H3cDHCPServerAllocateThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDHCPServerAllocateThreshold_Type.__name__=_C
_H3cDHCPServerAllocateThreshold_Object=MibScalar
h3cDHCPServerAllocateThreshold=_H3cDHCPServerAllocateThreshold_Object((1,3,6,1,4,1,2011,10,2,101,1,6),_H3cDHCPServerAllocateThreshold_Type())
h3cDHCPServerAllocateThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPServerAllocateThreshold.setStatus(_A)
_H3cDHCPServerTables_ObjectIdentity=ObjectIdentity
h3cDHCPServerTables=_H3cDHCPServerTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,101,2))
class _H3cDHCPServerPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDHCPServerPoolName_Type.__name__=_F
_H3cDHCPServerPoolName_Object=MibScalar
h3cDHCPServerPoolName=_H3cDHCPServerPoolName_Object((1,3,6,1,4,1,2011,10,2,101,2,1),_H3cDHCPServerPoolName_Type())
h3cDHCPServerPoolName.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cDHCPServerPoolName.setStatus(_A)
_H3cDHCPSrvGlobalPoolTable_Object=MibTable
h3cDHCPSrvGlobalPoolTable=_H3cDHCPSrvGlobalPoolTable_Object((1,3,6,1,4,1,2011,10,2,101,2,2))
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolTable.setStatus(_A)
_H3cDHCPSrvGlobalPoolEntry_Object=MibTableRow
h3cDHCPSrvGlobalPoolEntry=_H3cDHCPSrvGlobalPoolEntry_Object((1,3,6,1,4,1,2011,10,2,101,2,2,1))
h3cDHCPSrvGlobalPoolEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolEntry.setStatus(_A)
class _H3cDHCPSrvGlobalPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDHCPSrvGlobalPoolName_Type.__name__=_F
_H3cDHCPSrvGlobalPoolName_Object=MibTableColumn
h3cDHCPSrvGlobalPoolName=_H3cDHCPSrvGlobalPoolName_Object((1,3,6,1,4,1,2011,10,2,101,2,2,1,1),_H3cDHCPSrvGlobalPoolName_Type())
h3cDHCPSrvGlobalPoolName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolName.setStatus(_A)
_H3cDHCPSrvGlobalPoolRowStatus_Type=RowStatus
_H3cDHCPSrvGlobalPoolRowStatus_Object=MibTableColumn
h3cDHCPSrvGlobalPoolRowStatus=_H3cDHCPSrvGlobalPoolRowStatus_Object((1,3,6,1,4,1,2011,10,2,101,2,2,1,2),_H3cDHCPSrvGlobalPoolRowStatus_Type())
h3cDHCPSrvGlobalPoolRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolRowStatus.setStatus(_A)
_H3cDHCPSrvGlobalPoolConfigTable_Object=MibTable
h3cDHCPSrvGlobalPoolConfigTable=_H3cDHCPSrvGlobalPoolConfigTable_Object((1,3,6,1,4,1,2011,10,2,101,2,3))
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolConfigTable.setStatus(_A)
_H3cDHCPSrvGlobalPoolConfigEntry_Object=MibTableRow
h3cDHCPSrvGlobalPoolConfigEntry=_H3cDHCPSrvGlobalPoolConfigEntry_Object((1,3,6,1,4,1,2011,10,2,101,2,3,1))
h3cDHCPSrvGlobalPoolConfigEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolConfigEntry.setStatus(_A)
class _H3cDHCPSrvGlobalPoolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('null',0),('host',1),('network',2)))
_H3cDHCPSrvGlobalPoolType_Type.__name__=_C
_H3cDHCPSrvGlobalPoolType_Object=MibTableColumn
h3cDHCPSrvGlobalPoolType=_H3cDHCPSrvGlobalPoolType_Object((1,3,6,1,4,1,2011,10,2,101,2,3,1,1),_H3cDHCPSrvGlobalPoolType_Type())
h3cDHCPSrvGlobalPoolType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolType.setStatus(_A)
_H3cDHCPSrvGlobalPoolNetwork_Type=IpAddress
_H3cDHCPSrvGlobalPoolNetwork_Object=MibTableColumn
h3cDHCPSrvGlobalPoolNetwork=_H3cDHCPSrvGlobalPoolNetwork_Object((1,3,6,1,4,1,2011,10,2,101,2,3,1,2),_H3cDHCPSrvGlobalPoolNetwork_Type())
h3cDHCPSrvGlobalPoolNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolNetwork.setStatus(_A)
_H3cDHCPSrvGlobalPoolNetworkMask_Type=IpAddress
_H3cDHCPSrvGlobalPoolNetworkMask_Object=MibTableColumn
h3cDHCPSrvGlobalPoolNetworkMask=_H3cDHCPSrvGlobalPoolNetworkMask_Object((1,3,6,1,4,1,2011,10,2,101,2,3,1,3),_H3cDHCPSrvGlobalPoolNetworkMask_Type())
h3cDHCPSrvGlobalPoolNetworkMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolNetworkMask.setStatus(_A)
_H3cDHCPSrvGlobalPoolHostIPAddr_Type=IpAddress
_H3cDHCPSrvGlobalPoolHostIPAddr_Object=MibTableColumn
h3cDHCPSrvGlobalPoolHostIPAddr=_H3cDHCPSrvGlobalPoolHostIPAddr_Object((1,3,6,1,4,1,2011,10,2,101,2,3,1,4),_H3cDHCPSrvGlobalPoolHostIPAddr_Type())
h3cDHCPSrvGlobalPoolHostIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolHostIPAddr.setStatus(_A)
_H3cDHCPSrvGlobalPoolHostMask_Type=IpAddress
_H3cDHCPSrvGlobalPoolHostMask_Object=MibTableColumn
h3cDHCPSrvGlobalPoolHostMask=_H3cDHCPSrvGlobalPoolHostMask_Object((1,3,6,1,4,1,2011,10,2,101,2,3,1,5),_H3cDHCPSrvGlobalPoolHostMask_Type())
h3cDHCPSrvGlobalPoolHostMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolHostMask.setStatus(_A)
_H3cDHCPSrvGlobalPoolHostHAddr_Type=MacAddress
_H3cDHCPSrvGlobalPoolHostHAddr_Object=MibTableColumn
h3cDHCPSrvGlobalPoolHostHAddr=_H3cDHCPSrvGlobalPoolHostHAddr_Object((1,3,6,1,4,1,2011,10,2,101,2,3,1,6),_H3cDHCPSrvGlobalPoolHostHAddr_Type())
h3cDHCPSrvGlobalPoolHostHAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolHostHAddr.setStatus(_A)
class _H3cDHCPSrvGlobalPoolCfgUndoFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('undonetworkip',1),('undohostip',2),('undohosthaddr',3)))
_H3cDHCPSrvGlobalPoolCfgUndoFlag_Type.__name__=_C
_H3cDHCPSrvGlobalPoolCfgUndoFlag_Object=MibTableColumn
h3cDHCPSrvGlobalPoolCfgUndoFlag=_H3cDHCPSrvGlobalPoolCfgUndoFlag_Object((1,3,6,1,4,1,2011,10,2,101,2,3,1,7),_H3cDHCPSrvGlobalPoolCfgUndoFlag_Type())
h3cDHCPSrvGlobalPoolCfgUndoFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolCfgUndoFlag.setStatus(_A)
_H3cDHCPSrvGlobalPoolStartAddr_Type=IpAddress
_H3cDHCPSrvGlobalPoolStartAddr_Object=MibTableColumn
h3cDHCPSrvGlobalPoolStartAddr=_H3cDHCPSrvGlobalPoolStartAddr_Object((1,3,6,1,4,1,2011,10,2,101,2,3,1,8),_H3cDHCPSrvGlobalPoolStartAddr_Type())
h3cDHCPSrvGlobalPoolStartAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolStartAddr.setStatus(_A)
_H3cDHCPSrvGlobalPoolEndAddr_Type=IpAddress
_H3cDHCPSrvGlobalPoolEndAddr_Object=MibTableColumn
h3cDHCPSrvGlobalPoolEndAddr=_H3cDHCPSrvGlobalPoolEndAddr_Object((1,3,6,1,4,1,2011,10,2,101,2,3,1,9),_H3cDHCPSrvGlobalPoolEndAddr_Type())
h3cDHCPSrvGlobalPoolEndAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolEndAddr.setStatus(_A)
class _H3cDHCPSrvGlobalPoolAllocObject_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('user',0),('admin',1)))
_H3cDHCPSrvGlobalPoolAllocObject_Type.__name__=_C
_H3cDHCPSrvGlobalPoolAllocObject_Object=MibTableColumn
h3cDHCPSrvGlobalPoolAllocObject=_H3cDHCPSrvGlobalPoolAllocObject_Object((1,3,6,1,4,1,2011,10,2,101,2,3,1,10),_H3cDHCPSrvGlobalPoolAllocObject_Type())
h3cDHCPSrvGlobalPoolAllocObject.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolAllocObject.setStatus(_A)
_H3cDHCPSrvGlobalPoolParaTable_Object=MibTable
h3cDHCPSrvGlobalPoolParaTable=_H3cDHCPSrvGlobalPoolParaTable_Object((1,3,6,1,4,1,2011,10,2,101,2,4))
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolParaTable.setStatus(_A)
_H3cDHCPSrvGlobalPoolParaEntry_Object=MibTableRow
h3cDHCPSrvGlobalPoolParaEntry=_H3cDHCPSrvGlobalPoolParaEntry_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1))
h3cDHCPSrvGlobalPoolParaEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolParaEntry.setStatus(_A)
class _H3cDHCPSrvGlbPoolLeaseDay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,365))
_H3cDHCPSrvGlbPoolLeaseDay_Type.__name__=_C
_H3cDHCPSrvGlbPoolLeaseDay_Object=MibTableColumn
h3cDHCPSrvGlbPoolLeaseDay=_H3cDHCPSrvGlbPoolLeaseDay_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,1),_H3cDHCPSrvGlbPoolLeaseDay_Type())
h3cDHCPSrvGlbPoolLeaseDay.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolLeaseDay.setStatus(_A)
class _H3cDHCPSrvGlbPoolLeaseHour_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_H3cDHCPSrvGlbPoolLeaseHour_Type.__name__=_C
_H3cDHCPSrvGlbPoolLeaseHour_Object=MibTableColumn
h3cDHCPSrvGlbPoolLeaseHour=_H3cDHCPSrvGlbPoolLeaseHour_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,2),_H3cDHCPSrvGlbPoolLeaseHour_Type())
h3cDHCPSrvGlbPoolLeaseHour.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolLeaseHour.setStatus(_A)
class _H3cDHCPSrvGlbPoolLeaseMinute_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_H3cDHCPSrvGlbPoolLeaseMinute_Type.__name__=_C
_H3cDHCPSrvGlbPoolLeaseMinute_Object=MibTableColumn
h3cDHCPSrvGlbPoolLeaseMinute=_H3cDHCPSrvGlbPoolLeaseMinute_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,3),_H3cDHCPSrvGlbPoolLeaseMinute_Type())
h3cDHCPSrvGlbPoolLeaseMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolLeaseMinute.setStatus(_A)
class _H3cDHCPSrvGlbPoolLeaseUnlimited_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('invalid',0),('unlimited',1)))
_H3cDHCPSrvGlbPoolLeaseUnlimited_Type.__name__=_C
_H3cDHCPSrvGlbPoolLeaseUnlimited_Object=MibTableColumn
h3cDHCPSrvGlbPoolLeaseUnlimited=_H3cDHCPSrvGlbPoolLeaseUnlimited_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,4),_H3cDHCPSrvGlbPoolLeaseUnlimited_Type())
h3cDHCPSrvGlbPoolLeaseUnlimited.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolLeaseUnlimited.setStatus(_A)
class _H3cDHCPSrvGlbPoolDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDHCPSrvGlbPoolDomainName_Type.__name__=_F
_H3cDHCPSrvGlbPoolDomainName_Object=MibTableColumn
h3cDHCPSrvGlbPoolDomainName=_H3cDHCPSrvGlbPoolDomainName_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,5),_H3cDHCPSrvGlbPoolDomainName_Type())
h3cDHCPSrvGlbPoolDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolDomainName.setStatus(_A)
class _H3cDHCPSrvGlbPoolCliGWIPStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,129))
_H3cDHCPSrvGlbPoolCliGWIPStr_Type.__name__=_F
_H3cDHCPSrvGlbPoolCliGWIPStr_Object=MibTableColumn
h3cDHCPSrvGlbPoolCliGWIPStr=_H3cDHCPSrvGlbPoolCliGWIPStr_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,6),_H3cDHCPSrvGlbPoolCliGWIPStr_Type())
h3cDHCPSrvGlbPoolCliGWIPStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolCliGWIPStr.setStatus(_A)
_H3cDHCPSrvGlbPoolCliGWIPUndo_Type=IpAddress
_H3cDHCPSrvGlbPoolCliGWIPUndo_Object=MibTableColumn
h3cDHCPSrvGlbPoolCliGWIPUndo=_H3cDHCPSrvGlbPoolCliGWIPUndo_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,7),_H3cDHCPSrvGlbPoolCliGWIPUndo_Type())
h3cDHCPSrvGlbPoolCliGWIPUndo.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolCliGWIPUndo.setStatus(_A)
class _H3cDHCPSrvGlbPoolCliDNSIPStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,129))
_H3cDHCPSrvGlbPoolCliDNSIPStr_Type.__name__=_F
_H3cDHCPSrvGlbPoolCliDNSIPStr_Object=MibTableColumn
h3cDHCPSrvGlbPoolCliDNSIPStr=_H3cDHCPSrvGlbPoolCliDNSIPStr_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,8),_H3cDHCPSrvGlbPoolCliDNSIPStr_Type())
h3cDHCPSrvGlbPoolCliDNSIPStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolCliDNSIPStr.setStatus(_A)
_H3cDHCPSrvGlbPoolCliDNSIPUndo_Type=IpAddress
_H3cDHCPSrvGlbPoolCliDNSIPUndo_Object=MibTableColumn
h3cDHCPSrvGlbPoolCliDNSIPUndo=_H3cDHCPSrvGlbPoolCliDNSIPUndo_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,9),_H3cDHCPSrvGlbPoolCliDNSIPUndo_Type())
h3cDHCPSrvGlbPoolCliDNSIPUndo.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolCliDNSIPUndo.setStatus(_A)
class _H3cDHCPSrvGlbPoolCliNetbiosType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*(('null',0),('bnode',1),('pnode',2),('mnode',4),('hnode',8)))
_H3cDHCPSrvGlbPoolCliNetbiosType_Type.__name__=_C
_H3cDHCPSrvGlbPoolCliNetbiosType_Object=MibTableColumn
h3cDHCPSrvGlbPoolCliNetbiosType=_H3cDHCPSrvGlbPoolCliNetbiosType_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,10),_H3cDHCPSrvGlbPoolCliNetbiosType_Type())
h3cDHCPSrvGlbPoolCliNetbiosType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolCliNetbiosType.setStatus(_A)
class _H3cDHCPSrvGlbPoolCliNbnsIPStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,129))
_H3cDHCPSrvGlbPoolCliNbnsIPStr_Type.__name__=_F
_H3cDHCPSrvGlbPoolCliNbnsIPStr_Object=MibTableColumn
h3cDHCPSrvGlbPoolCliNbnsIPStr=_H3cDHCPSrvGlbPoolCliNbnsIPStr_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,11),_H3cDHCPSrvGlbPoolCliNbnsIPStr_Type())
h3cDHCPSrvGlbPoolCliNbnsIPStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolCliNbnsIPStr.setStatus(_A)
_H3cDHCPSrvGlbPoolCliNbnsIPUndo_Type=IpAddress
_H3cDHCPSrvGlbPoolCliNbnsIPUndo_Object=MibTableColumn
h3cDHCPSrvGlbPoolCliNbnsIPUndo=_H3cDHCPSrvGlbPoolCliNbnsIPUndo_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,12),_H3cDHCPSrvGlbPoolCliNbnsIPUndo_Type())
h3cDHCPSrvGlbPoolCliNbnsIPUndo.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolCliNbnsIPUndo.setStatus(_A)
class _H3cDHCPSrvGlbPoolParaUndoFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('undoDomain',1),('undoLease',2),('undoGateway',3),('undoDns',4),('undoNbns',5),('undoNbType',6)))
_H3cDHCPSrvGlbPoolParaUndoFlag_Type.__name__=_C
_H3cDHCPSrvGlbPoolParaUndoFlag_Object=MibTableColumn
h3cDHCPSrvGlbPoolParaUndoFlag=_H3cDHCPSrvGlbPoolParaUndoFlag_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,13),_H3cDHCPSrvGlbPoolParaUndoFlag_Type())
h3cDHCPSrvGlbPoolParaUndoFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolParaUndoFlag.setStatus(_A)
class _H3cDHCPSrvGlbPoolIPInUseReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_H3cDHCPSrvGlbPoolIPInUseReset_Type.__name__=_C
_H3cDHCPSrvGlbPoolIPInUseReset_Object=MibTableColumn
h3cDHCPSrvGlbPoolIPInUseReset=_H3cDHCPSrvGlbPoolIPInUseReset_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,14),_H3cDHCPSrvGlbPoolIPInUseReset_Type())
h3cDHCPSrvGlbPoolIPInUseReset.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolIPInUseReset.setStatus(_A)
_H3cDHCPSrvGlbPoolLeaseTime_Type=TimeTicks
_H3cDHCPSrvGlbPoolLeaseTime_Object=MibTableColumn
h3cDHCPSrvGlbPoolLeaseTime=_H3cDHCPSrvGlbPoolLeaseTime_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,15),_H3cDHCPSrvGlbPoolLeaseTime_Type())
h3cDHCPSrvGlbPoolLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolLeaseTime.setStatus(_A)
_H3cDHCPSrvGlbPoolPrimaryDNSIP_Type=IpAddress
_H3cDHCPSrvGlbPoolPrimaryDNSIP_Object=MibTableColumn
h3cDHCPSrvGlbPoolPrimaryDNSIP=_H3cDHCPSrvGlbPoolPrimaryDNSIP_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,16),_H3cDHCPSrvGlbPoolPrimaryDNSIP_Type())
h3cDHCPSrvGlbPoolPrimaryDNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolPrimaryDNSIP.setStatus(_A)
_H3cDHCPSrvGlbPoolSecondaryDNSIP_Type=IpAddress
_H3cDHCPSrvGlbPoolSecondaryDNSIP_Object=MibTableColumn
h3cDHCPSrvGlbPoolSecondaryDNSIP=_H3cDHCPSrvGlbPoolSecondaryDNSIP_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,17),_H3cDHCPSrvGlbPoolSecondaryDNSIP_Type())
h3cDHCPSrvGlbPoolSecondaryDNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolSecondaryDNSIP.setStatus(_A)
class _H3cDHCPSrvGlbPoolLeaseSecond_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_H3cDHCPSrvGlbPoolLeaseSecond_Type.__name__=_C
_H3cDHCPSrvGlbPoolLeaseSecond_Object=MibTableColumn
h3cDHCPSrvGlbPoolLeaseSecond=_H3cDHCPSrvGlbPoolLeaseSecond_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,18),_H3cDHCPSrvGlbPoolLeaseSecond_Type())
h3cDHCPSrvGlbPoolLeaseSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolLeaseSecond.setStatus(_A)
class _H3cDHCPSrvGlbPoolLeaseTimeSec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,31622399))
_H3cDHCPSrvGlbPoolLeaseTimeSec_Type.__name__=_C
_H3cDHCPSrvGlbPoolLeaseTimeSec_Object=MibTableColumn
h3cDHCPSrvGlbPoolLeaseTimeSec=_H3cDHCPSrvGlbPoolLeaseTimeSec_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,19),_H3cDHCPSrvGlbPoolLeaseTimeSec_Type())
h3cDHCPSrvGlbPoolLeaseTimeSec.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolLeaseTimeSec.setStatus(_A)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolLeaseTimeSec.setUnits('seconds')
_H3cDHCPSrvGlbPoolCliGWIPAddr_Type=IpAddress
_H3cDHCPSrvGlbPoolCliGWIPAddr_Object=MibTableColumn
h3cDHCPSrvGlbPoolCliGWIPAddr=_H3cDHCPSrvGlbPoolCliGWIPAddr_Object((1,3,6,1,4,1,2011,10,2,101,2,4,1,20),_H3cDHCPSrvGlbPoolCliGWIPAddr_Type())
h3cDHCPSrvGlbPoolCliGWIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolCliGWIPAddr.setStatus(_A)
_H3cDHCPSrvGlobalPoolOptionTable_Object=MibTable
h3cDHCPSrvGlobalPoolOptionTable=_H3cDHCPSrvGlobalPoolOptionTable_Object((1,3,6,1,4,1,2011,10,2,101,2,5))
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolOptionTable.setStatus(_A)
_H3cDHCPSrvGlobalPoolOptionEntry_Object=MibTableRow
h3cDHCPSrvGlobalPoolOptionEntry=_H3cDHCPSrvGlobalPoolOptionEntry_Object((1,3,6,1,4,1,2011,10,2,101,2,5,1))
h3cDHCPSrvGlobalPoolOptionEntry.setIndexNames((0,_D,_H),(0,_D,_M))
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolOptionEntry.setStatus(_A)
class _H3cDHCPSrvGlbPoolOptCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_H3cDHCPSrvGlbPoolOptCode_Type.__name__=_C
_H3cDHCPSrvGlbPoolOptCode_Object=MibTableColumn
h3cDHCPSrvGlbPoolOptCode=_H3cDHCPSrvGlbPoolOptCode_Object((1,3,6,1,4,1,2011,10,2,101,2,5,1,1),_H3cDHCPSrvGlbPoolOptCode_Type())
h3cDHCPSrvGlbPoolOptCode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolOptCode.setStatus(_A)
class _H3cDHCPSrvGlbPoolOptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ascii',1),('hex',2),('ip',3)))
_H3cDHCPSrvGlbPoolOptType_Type.__name__=_C
_H3cDHCPSrvGlbPoolOptType_Object=MibTableColumn
h3cDHCPSrvGlbPoolOptType=_H3cDHCPSrvGlbPoolOptType_Object((1,3,6,1,4,1,2011,10,2,101,2,5,1,2),_H3cDHCPSrvGlbPoolOptType_Type())
h3cDHCPSrvGlbPoolOptType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolOptType.setStatus(_A)
class _H3cDHCPSrvGlbPoolOptAscii_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cDHCPSrvGlbPoolOptAscii_Type.__name__=_F
_H3cDHCPSrvGlbPoolOptAscii_Object=MibTableColumn
h3cDHCPSrvGlbPoolOptAscii=_H3cDHCPSrvGlbPoolOptAscii_Object((1,3,6,1,4,1,2011,10,2,101,2,5,1,3),_H3cDHCPSrvGlbPoolOptAscii_Type())
h3cDHCPSrvGlbPoolOptAscii.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolOptAscii.setStatus(_A)
class _H3cDHCPSrvGlbPoolOptHexString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,573))
_H3cDHCPSrvGlbPoolOptHexString_Type.__name__=_F
_H3cDHCPSrvGlbPoolOptHexString_Object=MibTableColumn
h3cDHCPSrvGlbPoolOptHexString=_H3cDHCPSrvGlbPoolOptHexString_Object((1,3,6,1,4,1,2011,10,2,101,2,5,1,4),_H3cDHCPSrvGlbPoolOptHexString_Type())
h3cDHCPSrvGlbPoolOptHexString.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolOptHexString.setStatus(_A)
class _H3cDHCPSrvGlbPoolOptIPString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,129))
_H3cDHCPSrvGlbPoolOptIPString_Type.__name__=_F
_H3cDHCPSrvGlbPoolOptIPString_Object=MibTableColumn
h3cDHCPSrvGlbPoolOptIPString=_H3cDHCPSrvGlbPoolOptIPString_Object((1,3,6,1,4,1,2011,10,2,101,2,5,1,5),_H3cDHCPSrvGlbPoolOptIPString_Type())
h3cDHCPSrvGlbPoolOptIPString.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolOptIPString.setStatus(_A)
_H3cDHCPSrvGlbPoolOptRowStatus_Type=RowStatus
_H3cDHCPSrvGlbPoolOptRowStatus_Object=MibTableColumn
h3cDHCPSrvGlbPoolOptRowStatus=_H3cDHCPSrvGlbPoolOptRowStatus_Object((1,3,6,1,4,1,2011,10,2,101,2,5,1,6),_H3cDHCPSrvGlbPoolOptRowStatus_Type())
h3cDHCPSrvGlbPoolOptRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolOptRowStatus.setStatus(_A)
_H3cDHCPSrvGlobalPoolStatTable_Object=MibTable
h3cDHCPSrvGlobalPoolStatTable=_H3cDHCPSrvGlobalPoolStatTable_Object((1,3,6,1,4,1,2011,10,2,101,2,6))
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolStatTable.setStatus(_A)
_H3cDHCPSrvGlobalPoolStatEntry_Object=MibTableRow
h3cDHCPSrvGlobalPoolStatEntry=_H3cDHCPSrvGlobalPoolStatEntry_Object((1,3,6,1,4,1,2011,10,2,101,2,6,1))
h3cDHCPSrvGlobalPoolStatEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cDHCPSrvGlobalPoolStatEntry.setStatus(_A)
_H3cDHCPSrvGlbPoolIPPoolUsage_Type=Integer32
_H3cDHCPSrvGlbPoolIPPoolUsage_Object=MibTableColumn
h3cDHCPSrvGlbPoolIPPoolUsage=_H3cDHCPSrvGlbPoolIPPoolUsage_Object((1,3,6,1,4,1,2011,10,2,101,2,6,1,1),_H3cDHCPSrvGlbPoolIPPoolUsage_Type())
h3cDHCPSrvGlbPoolIPPoolUsage.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolIPPoolUsage.setStatus(_A)
_H3cDHCPSrvGlbPoolReqTimes_Type=Counter32
_H3cDHCPSrvGlbPoolReqTimes_Object=MibTableColumn
h3cDHCPSrvGlbPoolReqTimes=_H3cDHCPSrvGlbPoolReqTimes_Object((1,3,6,1,4,1,2011,10,2,101,2,6,1,2),_H3cDHCPSrvGlbPoolReqTimes_Type())
h3cDHCPSrvGlbPoolReqTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolReqTimes.setStatus(_A)
_H3cDHCPSrvGlbPoolSuccessTimes_Type=Counter32
_H3cDHCPSrvGlbPoolSuccessTimes_Object=MibTableColumn
h3cDHCPSrvGlbPoolSuccessTimes=_H3cDHCPSrvGlbPoolSuccessTimes_Object((1,3,6,1,4,1,2011,10,2,101,2,6,1,3),_H3cDHCPSrvGlbPoolSuccessTimes_Type())
h3cDHCPSrvGlbPoolSuccessTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolSuccessTimes.setStatus(_A)
_H3cDHCPSrvGlbPoolDiscoverTimes_Type=Counter32
_H3cDHCPSrvGlbPoolDiscoverTimes_Object=MibTableColumn
h3cDHCPSrvGlbPoolDiscoverTimes=_H3cDHCPSrvGlbPoolDiscoverTimes_Object((1,3,6,1,4,1,2011,10,2,101,2,6,1,4),_H3cDHCPSrvGlbPoolDiscoverTimes_Type())
h3cDHCPSrvGlbPoolDiscoverTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolDiscoverTimes.setStatus(_A)
_H3cDHCPSrvGlbPoolOfferTimes_Type=Counter32
_H3cDHCPSrvGlbPoolOfferTimes_Object=MibTableColumn
h3cDHCPSrvGlbPoolOfferTimes=_H3cDHCPSrvGlbPoolOfferTimes_Object((1,3,6,1,4,1,2011,10,2,101,2,6,1,5),_H3cDHCPSrvGlbPoolOfferTimes_Type())
h3cDHCPSrvGlbPoolOfferTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolOfferTimes.setStatus(_A)
_H3cDHCPSrvGlbPoolACKTimes_Type=Counter32
_H3cDHCPSrvGlbPoolACKTimes_Object=MibTableColumn
h3cDHCPSrvGlbPoolACKTimes=_H3cDHCPSrvGlbPoolACKTimes_Object((1,3,6,1,4,1,2011,10,2,101,2,6,1,6),_H3cDHCPSrvGlbPoolACKTimes_Type())
h3cDHCPSrvGlbPoolACKTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolACKTimes.setStatus(_A)
_H3cDHCPSrvGlbPoolTotalIpNum_Type=Counter32
_H3cDHCPSrvGlbPoolTotalIpNum_Object=MibTableColumn
h3cDHCPSrvGlbPoolTotalIpNum=_H3cDHCPSrvGlbPoolTotalIpNum_Object((1,3,6,1,4,1,2011,10,2,101,2,6,1,7),_H3cDHCPSrvGlbPoolTotalIpNum_Type())
h3cDHCPSrvGlbPoolTotalIpNum.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolTotalIpNum.setStatus(_A)
_H3cDHCPSrvGlbPoolInUsedIpNum_Type=Counter32
_H3cDHCPSrvGlbPoolInUsedIpNum_Object=MibTableColumn
h3cDHCPSrvGlbPoolInUsedIpNum=_H3cDHCPSrvGlbPoolInUsedIpNum_Object((1,3,6,1,4,1,2011,10,2,101,2,6,1,8),_H3cDHCPSrvGlbPoolInUsedIpNum_Type())
h3cDHCPSrvGlbPoolInUsedIpNum.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSrvGlbPoolInUsedIpNum.setStatus(_A)
_H3cDHCPSvrOptionGroupTable_Object=MibTable
h3cDHCPSvrOptionGroupTable=_H3cDHCPSvrOptionGroupTable_Object((1,3,6,1,4,1,2011,10,2,101,2,7))
if mibBuilder.loadTexts:h3cDHCPSvrOptionGroupTable.setStatus(_A)
_H3cDHCPSvrOptionGroupEntry_Object=MibTableRow
h3cDHCPSvrOptionGroupEntry=_H3cDHCPSvrOptionGroupEntry_Object((1,3,6,1,4,1,2011,10,2,101,2,7,1))
h3cDHCPSvrOptionGroupEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:h3cDHCPSvrOptionGroupEntry.setStatus(_A)
class _H3cDHCPSvrOptionGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cDHCPSvrOptionGroupIndex_Type.__name__=_C
_H3cDHCPSvrOptionGroupIndex_Object=MibTableColumn
h3cDHCPSvrOptionGroupIndex=_H3cDHCPSvrOptionGroupIndex_Object((1,3,6,1,4,1,2011,10,2,101,2,7,1,1),_H3cDHCPSvrOptionGroupIndex_Type())
h3cDHCPSvrOptionGroupIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSvrOptionGroupIndex.setStatus(_A)
_H3cDHCPSvrOptionGroupRowstatus_Type=RowStatus
_H3cDHCPSvrOptionGroupRowstatus_Object=MibTableColumn
h3cDHCPSvrOptionGroupRowstatus=_H3cDHCPSvrOptionGroupRowstatus_Object((1,3,6,1,4,1,2011,10,2,101,2,7,1,2),_H3cDHCPSvrOptionGroupRowstatus_Type())
h3cDHCPSvrOptionGroupRowstatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSvrOptionGroupRowstatus.setStatus(_A)
_H3cDHCPSvrOptionTable_Object=MibTable
h3cDHCPSvrOptionTable=_H3cDHCPSvrOptionTable_Object((1,3,6,1,4,1,2011,10,2,101,2,8))
if mibBuilder.loadTexts:h3cDHCPSvrOptionTable.setStatus(_A)
_H3cDHCPSvrOptionEntry_Object=MibTableRow
h3cDHCPSvrOptionEntry=_H3cDHCPSvrOptionEntry_Object((1,3,6,1,4,1,2011,10,2,101,2,8,1))
h3cDHCPSvrOptionEntry.setIndexNames((0,_D,_J),(0,_D,_N))
if mibBuilder.loadTexts:h3cDHCPSvrOptionEntry.setStatus(_A)
class _H3cDHCPSvrOptionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_H3cDHCPSvrOptionCode_Type.__name__=_C
_H3cDHCPSvrOptionCode_Object=MibTableColumn
h3cDHCPSvrOptionCode=_H3cDHCPSvrOptionCode_Object((1,3,6,1,4,1,2011,10,2,101,2,8,1,1),_H3cDHCPSvrOptionCode_Type())
h3cDHCPSvrOptionCode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSvrOptionCode.setStatus(_A)
class _H3cDHCPSvrOptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ascii',1),('hex',2),('ip',3)))
_H3cDHCPSvrOptionType_Type.__name__=_C
_H3cDHCPSvrOptionType_Object=MibTableColumn
h3cDHCPSvrOptionType=_H3cDHCPSvrOptionType_Object((1,3,6,1,4,1,2011,10,2,101,2,8,1,2),_H3cDHCPSvrOptionType_Type())
h3cDHCPSvrOptionType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSvrOptionType.setStatus(_A)
class _H3cDHCPSvrOptionAsciiString_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDHCPSvrOptionAsciiString_Type.__name__=_F
_H3cDHCPSvrOptionAsciiString_Object=MibTableColumn
h3cDHCPSvrOptionAsciiString=_H3cDHCPSvrOptionAsciiString_Object((1,3,6,1,4,1,2011,10,2,101,2,8,1,3),_H3cDHCPSvrOptionAsciiString_Type())
h3cDHCPSvrOptionAsciiString.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSvrOptionAsciiString.setStatus(_A)
class _H3cDHCPSvrOptionHexString_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,573))
_H3cDHCPSvrOptionHexString_Type.__name__=_F
_H3cDHCPSvrOptionHexString_Object=MibTableColumn
h3cDHCPSvrOptionHexString=_H3cDHCPSvrOptionHexString_Object((1,3,6,1,4,1,2011,10,2,101,2,8,1,4),_H3cDHCPSvrOptionHexString_Type())
h3cDHCPSvrOptionHexString.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSvrOptionHexString.setStatus(_A)
class _H3cDHCPSvrOptionIPString_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,129))
_H3cDHCPSvrOptionIPString_Type.__name__=_F
_H3cDHCPSvrOptionIPString_Object=MibTableColumn
h3cDHCPSvrOptionIPString=_H3cDHCPSvrOptionIPString_Object((1,3,6,1,4,1,2011,10,2,101,2,8,1,5),_H3cDHCPSvrOptionIPString_Type())
h3cDHCPSvrOptionIPString.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSvrOptionIPString.setStatus(_A)
_H3cDHCPSvrOptionRowstatus_Type=RowStatus
_H3cDHCPSvrOptionRowstatus_Object=MibTableColumn
h3cDHCPSvrOptionRowstatus=_H3cDHCPSvrOptionRowstatus_Object((1,3,6,1,4,1,2011,10,2,101,2,8,1,6),_H3cDHCPSvrOptionRowstatus_Type())
h3cDHCPSvrOptionRowstatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSvrOptionRowstatus.setStatus(_A)
_H3cDHCPSvrVerifyMacTable_Object=MibTable
h3cDHCPSvrVerifyMacTable=_H3cDHCPSvrVerifyMacTable_Object((1,3,6,1,4,1,2011,10,2,101,2,9))
if mibBuilder.loadTexts:h3cDHCPSvrVerifyMacTable.setStatus(_A)
_H3cDHCPSvrVerifyMacEntry_Object=MibTableRow
h3cDHCPSvrVerifyMacEntry=_H3cDHCPSvrVerifyMacEntry_Object((1,3,6,1,4,1,2011,10,2,101,2,9,1))
h3cDHCPSvrVerifyMacEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cDHCPSvrVerifyMacEntry.setStatus(_A)
class _H3cDHCPSvrVerifyMacSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_H3cDHCPSvrVerifyMacSwitch_Type.__name__=_C
_H3cDHCPSvrVerifyMacSwitch_Object=MibTableColumn
h3cDHCPSvrVerifyMacSwitch=_H3cDHCPSvrVerifyMacSwitch_Object((1,3,6,1,4,1,2011,10,2,101,2,9,1,1),_H3cDHCPSvrVerifyMacSwitch_Type())
h3cDHCPSvrVerifyMacSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSvrVerifyMacSwitch.setStatus(_A)
_H3cDHCPSvrPoolMacTable_Object=MibTable
h3cDHCPSvrPoolMacTable=_H3cDHCPSvrPoolMacTable_Object((1,3,6,1,4,1,2011,10,2,101,2,10))
if mibBuilder.loadTexts:h3cDHCPSvrPoolMacTable.setStatus(_A)
_H3cDHCPSvrPoolMacEntry_Object=MibTableRow
h3cDHCPSvrPoolMacEntry=_H3cDHCPSvrPoolMacEntry_Object((1,3,6,1,4,1,2011,10,2,101,2,10,1))
h3cDHCPSvrPoolMacEntry.setIndexNames((0,_D,_H),(0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:h3cDHCPSvrPoolMacEntry.setStatus(_A)
_H3cDHCPSvrPoolMac_Type=MacAddress
_H3cDHCPSvrPoolMac_Object=MibTableColumn
h3cDHCPSvrPoolMac=_H3cDHCPSvrPoolMac_Object((1,3,6,1,4,1,2011,10,2,101,2,10,1,1),_H3cDHCPSvrPoolMac_Type())
h3cDHCPSvrPoolMac.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSvrPoolMac.setStatus(_A)
_H3cDHCPSvrPoolMacMask_Type=MacAddress
_H3cDHCPSvrPoolMacMask_Object=MibTableColumn
h3cDHCPSvrPoolMacMask=_H3cDHCPSvrPoolMacMask_Object((1,3,6,1,4,1,2011,10,2,101,2,10,1,2),_H3cDHCPSvrPoolMacMask_Type())
h3cDHCPSvrPoolMacMask.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDHCPSvrPoolMacMask.setStatus(_A)
class _H3cDHCPSvrPoolMacOptIndex_Type(Integer32):defaultValue=0
_H3cDHCPSvrPoolMacOptIndex_Type.__name__=_C
_H3cDHCPSvrPoolMacOptIndex_Object=MibTableColumn
h3cDHCPSvrPoolMacOptIndex=_H3cDHCPSvrPoolMacOptIndex_Object((1,3,6,1,4,1,2011,10,2,101,2,10,1,3),_H3cDHCPSvrPoolMacOptIndex_Type())
h3cDHCPSvrPoolMacOptIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPSvrPoolMacOptIndex.setStatus(_A)
_H3cDHCPSvrPoolMacRowstatus_Type=RowStatus
_H3cDHCPSvrPoolMacRowstatus_Object=MibTableColumn
h3cDHCPSvrPoolMacRowstatus=_H3cDHCPSvrPoolMacRowstatus_Object((1,3,6,1,4,1,2011,10,2,101,2,10,1,4),_H3cDHCPSvrPoolMacRowstatus_Type())
h3cDHCPSvrPoolMacRowstatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDHCPSvrPoolMacRowstatus.setStatus(_A)
_H3cDHCPServerTraps_ObjectIdentity=ObjectIdentity
h3cDHCPServerTraps=_H3cDHCPServerTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,101,3))
_H3cDHCPServerTrapPrefix_ObjectIdentity=ObjectIdentity
h3cDHCPServerTrapPrefix=_H3cDHCPServerTrapPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,101,3,0))
_H3cDHCPServerTrapObjects_ObjectIdentity=ObjectIdentity
h3cDHCPServerTrapObjects=_H3cDHCPServerTrapObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,101,3,1))
_H3cDHCPServerFirstTrapTime_Type=TimeTicks
_H3cDHCPServerFirstTrapTime_Object=MibScalar
h3cDHCPServerFirstTrapTime=_H3cDHCPServerFirstTrapTime_Object((1,3,6,1,4,1,2011,10,2,101,3,1,1),_H3cDHCPServerFirstTrapTime_Type())
h3cDHCPServerFirstTrapTime.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cDHCPServerFirstTrapTime.setStatus(_A)
h3cDHCPServerAddrExhaust=NotificationType((1,3,6,1,4,1,2011,10,2,101,3,0,1))
h3cDHCPServerAddrExhaust.setObjects(*((_D,_I),(_D,_K)))
if mibBuilder.loadTexts:h3cDHCPServerAddrExhaust.setStatus(_A)
h3cDHCPServerAddrExhaustRecover=NotificationType((1,3,6,1,4,1,2011,10,2,101,3,0,2))
h3cDHCPServerAddrExhaustRecover.setObjects(*((_D,_I),(_D,_K)))
if mibBuilder.loadTexts:h3cDHCPServerAddrExhaustRecover.setStatus(_A)
h3cDHCPServerAvgIpUsageOverflow=NotificationType((1,3,6,1,4,1,2011,10,2,101,3,0,3))
h3cDHCPServerAvgIpUsageOverflow.setObjects((_D,_I))
if mibBuilder.loadTexts:h3cDHCPServerAvgIpUsageOverflow.setStatus(_A)
h3cDHCPServerMaxIpUsageOverflow=NotificationType((1,3,6,1,4,1,2011,10,2,101,3,0,4))
h3cDHCPServerMaxIpUsageOverflow.setObjects((_D,_I))
if mibBuilder.loadTexts:h3cDHCPServerMaxIpUsageOverflow.setStatus(_A)
h3cDHCPServerAllocateOverflow=NotificationType((1,3,6,1,4,1,2011,10,2,101,3,0,5))
if mibBuilder.loadTexts:h3cDHCPServerAllocateOverflow.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cDHCPServer':h3cDHCPServer,'h3cDHCPServerObjects':h3cDHCPServerObjects,'h3cDHCPServerIPPoolUsage':h3cDHCPServerIPPoolUsage,'h3cDHCPServerReqTimes':h3cDHCPServerReqTimes,'h3cDHCPServerReqSuccessTimes':h3cDHCPServerReqSuccessTimes,'h3cDHCPServerAvgIpUseThreshold':h3cDHCPServerAvgIpUseThreshold,'h3cDHCPServerMaxIpUseThreshold':h3cDHCPServerMaxIpUseThreshold,'h3cDHCPServerAllocateThreshold':h3cDHCPServerAllocateThreshold,'h3cDHCPServerTables':h3cDHCPServerTables,_I:h3cDHCPServerPoolName,'h3cDHCPSrvGlobalPoolTable':h3cDHCPSrvGlobalPoolTable,'h3cDHCPSrvGlobalPoolEntry':h3cDHCPSrvGlobalPoolEntry,_H:h3cDHCPSrvGlobalPoolName,'h3cDHCPSrvGlobalPoolRowStatus':h3cDHCPSrvGlobalPoolRowStatus,'h3cDHCPSrvGlobalPoolConfigTable':h3cDHCPSrvGlobalPoolConfigTable,'h3cDHCPSrvGlobalPoolConfigEntry':h3cDHCPSrvGlobalPoolConfigEntry,'h3cDHCPSrvGlobalPoolType':h3cDHCPSrvGlobalPoolType,'h3cDHCPSrvGlobalPoolNetwork':h3cDHCPSrvGlobalPoolNetwork,'h3cDHCPSrvGlobalPoolNetworkMask':h3cDHCPSrvGlobalPoolNetworkMask,'h3cDHCPSrvGlobalPoolHostIPAddr':h3cDHCPSrvGlobalPoolHostIPAddr,'h3cDHCPSrvGlobalPoolHostMask':h3cDHCPSrvGlobalPoolHostMask,'h3cDHCPSrvGlobalPoolHostHAddr':h3cDHCPSrvGlobalPoolHostHAddr,'h3cDHCPSrvGlobalPoolCfgUndoFlag':h3cDHCPSrvGlobalPoolCfgUndoFlag,'h3cDHCPSrvGlobalPoolStartAddr':h3cDHCPSrvGlobalPoolStartAddr,'h3cDHCPSrvGlobalPoolEndAddr':h3cDHCPSrvGlobalPoolEndAddr,'h3cDHCPSrvGlobalPoolAllocObject':h3cDHCPSrvGlobalPoolAllocObject,'h3cDHCPSrvGlobalPoolParaTable':h3cDHCPSrvGlobalPoolParaTable,'h3cDHCPSrvGlobalPoolParaEntry':h3cDHCPSrvGlobalPoolParaEntry,'h3cDHCPSrvGlbPoolLeaseDay':h3cDHCPSrvGlbPoolLeaseDay,'h3cDHCPSrvGlbPoolLeaseHour':h3cDHCPSrvGlbPoolLeaseHour,'h3cDHCPSrvGlbPoolLeaseMinute':h3cDHCPSrvGlbPoolLeaseMinute,'h3cDHCPSrvGlbPoolLeaseUnlimited':h3cDHCPSrvGlbPoolLeaseUnlimited,'h3cDHCPSrvGlbPoolDomainName':h3cDHCPSrvGlbPoolDomainName,'h3cDHCPSrvGlbPoolCliGWIPStr':h3cDHCPSrvGlbPoolCliGWIPStr,'h3cDHCPSrvGlbPoolCliGWIPUndo':h3cDHCPSrvGlbPoolCliGWIPUndo,'h3cDHCPSrvGlbPoolCliDNSIPStr':h3cDHCPSrvGlbPoolCliDNSIPStr,'h3cDHCPSrvGlbPoolCliDNSIPUndo':h3cDHCPSrvGlbPoolCliDNSIPUndo,'h3cDHCPSrvGlbPoolCliNetbiosType':h3cDHCPSrvGlbPoolCliNetbiosType,'h3cDHCPSrvGlbPoolCliNbnsIPStr':h3cDHCPSrvGlbPoolCliNbnsIPStr,'h3cDHCPSrvGlbPoolCliNbnsIPUndo':h3cDHCPSrvGlbPoolCliNbnsIPUndo,'h3cDHCPSrvGlbPoolParaUndoFlag':h3cDHCPSrvGlbPoolParaUndoFlag,'h3cDHCPSrvGlbPoolIPInUseReset':h3cDHCPSrvGlbPoolIPInUseReset,'h3cDHCPSrvGlbPoolLeaseTime':h3cDHCPSrvGlbPoolLeaseTime,'h3cDHCPSrvGlbPoolPrimaryDNSIP':h3cDHCPSrvGlbPoolPrimaryDNSIP,'h3cDHCPSrvGlbPoolSecondaryDNSIP':h3cDHCPSrvGlbPoolSecondaryDNSIP,'h3cDHCPSrvGlbPoolLeaseSecond':h3cDHCPSrvGlbPoolLeaseSecond,'h3cDHCPSrvGlbPoolLeaseTimeSec':h3cDHCPSrvGlbPoolLeaseTimeSec,'h3cDHCPSrvGlbPoolCliGWIPAddr':h3cDHCPSrvGlbPoolCliGWIPAddr,'h3cDHCPSrvGlobalPoolOptionTable':h3cDHCPSrvGlobalPoolOptionTable,'h3cDHCPSrvGlobalPoolOptionEntry':h3cDHCPSrvGlobalPoolOptionEntry,_M:h3cDHCPSrvGlbPoolOptCode,'h3cDHCPSrvGlbPoolOptType':h3cDHCPSrvGlbPoolOptType,'h3cDHCPSrvGlbPoolOptAscii':h3cDHCPSrvGlbPoolOptAscii,'h3cDHCPSrvGlbPoolOptHexString':h3cDHCPSrvGlbPoolOptHexString,'h3cDHCPSrvGlbPoolOptIPString':h3cDHCPSrvGlbPoolOptIPString,'h3cDHCPSrvGlbPoolOptRowStatus':h3cDHCPSrvGlbPoolOptRowStatus,'h3cDHCPSrvGlobalPoolStatTable':h3cDHCPSrvGlobalPoolStatTable,'h3cDHCPSrvGlobalPoolStatEntry':h3cDHCPSrvGlobalPoolStatEntry,'h3cDHCPSrvGlbPoolIPPoolUsage':h3cDHCPSrvGlbPoolIPPoolUsage,'h3cDHCPSrvGlbPoolReqTimes':h3cDHCPSrvGlbPoolReqTimes,'h3cDHCPSrvGlbPoolSuccessTimes':h3cDHCPSrvGlbPoolSuccessTimes,'h3cDHCPSrvGlbPoolDiscoverTimes':h3cDHCPSrvGlbPoolDiscoverTimes,'h3cDHCPSrvGlbPoolOfferTimes':h3cDHCPSrvGlbPoolOfferTimes,'h3cDHCPSrvGlbPoolACKTimes':h3cDHCPSrvGlbPoolACKTimes,'h3cDHCPSrvGlbPoolTotalIpNum':h3cDHCPSrvGlbPoolTotalIpNum,'h3cDHCPSrvGlbPoolInUsedIpNum':h3cDHCPSrvGlbPoolInUsedIpNum,'h3cDHCPSvrOptionGroupTable':h3cDHCPSvrOptionGroupTable,'h3cDHCPSvrOptionGroupEntry':h3cDHCPSvrOptionGroupEntry,_J:h3cDHCPSvrOptionGroupIndex,'h3cDHCPSvrOptionGroupRowstatus':h3cDHCPSvrOptionGroupRowstatus,'h3cDHCPSvrOptionTable':h3cDHCPSvrOptionTable,'h3cDHCPSvrOptionEntry':h3cDHCPSvrOptionEntry,_N:h3cDHCPSvrOptionCode,'h3cDHCPSvrOptionType':h3cDHCPSvrOptionType,'h3cDHCPSvrOptionAsciiString':h3cDHCPSvrOptionAsciiString,'h3cDHCPSvrOptionHexString':h3cDHCPSvrOptionHexString,'h3cDHCPSvrOptionIPString':h3cDHCPSvrOptionIPString,'h3cDHCPSvrOptionRowstatus':h3cDHCPSvrOptionRowstatus,'h3cDHCPSvrVerifyMacTable':h3cDHCPSvrVerifyMacTable,'h3cDHCPSvrVerifyMacEntry':h3cDHCPSvrVerifyMacEntry,'h3cDHCPSvrVerifyMacSwitch':h3cDHCPSvrVerifyMacSwitch,'h3cDHCPSvrPoolMacTable':h3cDHCPSvrPoolMacTable,'h3cDHCPSvrPoolMacEntry':h3cDHCPSvrPoolMacEntry,_O:h3cDHCPSvrPoolMac,_P:h3cDHCPSvrPoolMacMask,'h3cDHCPSvrPoolMacOptIndex':h3cDHCPSvrPoolMacOptIndex,'h3cDHCPSvrPoolMacRowstatus':h3cDHCPSvrPoolMacRowstatus,'h3cDHCPServerTraps':h3cDHCPServerTraps,'h3cDHCPServerTrapPrefix':h3cDHCPServerTrapPrefix,'h3cDHCPServerAddrExhaust':h3cDHCPServerAddrExhaust,'h3cDHCPServerAddrExhaustRecover':h3cDHCPServerAddrExhaustRecover,'h3cDHCPServerAvgIpUsageOverflow':h3cDHCPServerAvgIpUsageOverflow,'h3cDHCPServerMaxIpUsageOverflow':h3cDHCPServerMaxIpUsageOverflow,'h3cDHCPServerAllocateOverflow':h3cDHCPServerAllocateOverflow,'h3cDHCPServerTrapObjects':h3cDHCPServerTrapObjects,_K:h3cDHCPServerFirstTrapTime})