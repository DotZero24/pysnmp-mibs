_M='zxDslTrafficIfLogicalId'
_L='zxDslTrafficIfCircuitType'
_K='zxDslTrafficIfIndex'
_J='zxDslTrafficSvcIface'
_I='zxDslTrafficPort'
_H='kbytes'
_G='zxDslTrafficConfPrfName'
_F='DisplayString'
_E='not-accessible'
_D='ZTE-DSL-TRAFFIC-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','TextualConvention')
zxDslTrafficMgmt=ModuleIdentity((1,3,6,1,4,1,3902,1004,42))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxDsl_ObjectIdentity=ObjectIdentity
zxDsl=_ZxDsl_ObjectIdentity((1,3,6,1,4,1,3902,1004))
_ZxDslTrafficConfProfileTable_Object=MibTable
zxDslTrafficConfProfileTable=_ZxDslTrafficConfProfileTable_Object((1,3,6,1,4,1,3902,1004,42,1))
if mibBuilder.loadTexts:zxDslTrafficConfProfileTable.setStatus(_A)
_ZxDslTrafficConfProfileEntry_Object=MibTableRow
zxDslTrafficConfProfileEntry=_ZxDslTrafficConfProfileEntry_Object((1,3,6,1,4,1,3902,1004,42,1,1))
zxDslTrafficConfProfileEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:zxDslTrafficConfProfileEntry.setStatus(_A)
class _ZxDslTrafficConfPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxDslTrafficConfPrfName_Type.__name__=_F
_ZxDslTrafficConfPrfName_Object=MibTableColumn
zxDslTrafficConfPrfName=_ZxDslTrafficConfPrfName_Object((1,3,6,1,4,1,3902,1004,42,1,1,1),_ZxDslTrafficConfPrfName_Type())
zxDslTrafficConfPrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslTrafficConfPrfName.setStatus(_A)
_ZxDslTrafficConfPrfCir_Type=Integer32
_ZxDslTrafficConfPrfCir_Object=MibTableColumn
zxDslTrafficConfPrfCir=_ZxDslTrafficConfPrfCir_Object((1,3,6,1,4,1,3902,1004,42,1,1,2),_ZxDslTrafficConfPrfCir_Type())
zxDslTrafficConfPrfCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficConfPrfCir.setStatus(_A)
if mibBuilder.loadTexts:zxDslTrafficConfPrfCir.setUnits('kbps')
_ZxDslTrafficConfPrfCbs_Type=Integer32
_ZxDslTrafficConfPrfCbs_Object=MibTableColumn
zxDslTrafficConfPrfCbs=_ZxDslTrafficConfPrfCbs_Object((1,3,6,1,4,1,3902,1004,42,1,1,3),_ZxDslTrafficConfPrfCbs_Type())
zxDslTrafficConfPrfCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficConfPrfCbs.setStatus(_A)
if mibBuilder.loadTexts:zxDslTrafficConfPrfCbs.setUnits(_H)
_ZxDslTrafficConfPrfPir_Type=Integer32
_ZxDslTrafficConfPrfPir_Object=MibTableColumn
zxDslTrafficConfPrfPir=_ZxDslTrafficConfPrfPir_Object((1,3,6,1,4,1,3902,1004,42,1,1,4),_ZxDslTrafficConfPrfPir_Type())
zxDslTrafficConfPrfPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficConfPrfPir.setStatus(_A)
if mibBuilder.loadTexts:zxDslTrafficConfPrfPir.setUnits('kbps')
_ZxDslTrafficConfPrfPbs_Type=Integer32
_ZxDslTrafficConfPrfPbs_Object=MibTableColumn
zxDslTrafficConfPrfPbs=_ZxDslTrafficConfPrfPbs_Object((1,3,6,1,4,1,3902,1004,42,1,1,5),_ZxDslTrafficConfPrfPbs_Type())
zxDslTrafficConfPrfPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficConfPrfPbs.setStatus(_A)
if mibBuilder.loadTexts:zxDslTrafficConfPrfPbs.setUnits(_H)
class _ZxDslTrafficConfPrfCosPriTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('override',1),('trust',2)))
_ZxDslTrafficConfPrfCosPriTrust_Type.__name__=_C
_ZxDslTrafficConfPrfCosPriTrust_Object=MibTableColumn
zxDslTrafficConfPrfCosPriTrust=_ZxDslTrafficConfPrfCosPriTrust_Object((1,3,6,1,4,1,3902,1004,42,1,1,6),_ZxDslTrafficConfPrfCosPriTrust_Type())
zxDslTrafficConfPrfCosPriTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficConfPrfCosPriTrust.setStatus(_A)
_ZxDslTrafficConfPrfCosPriority_Type=Integer32
_ZxDslTrafficConfPrfCosPriority_Object=MibTableColumn
zxDslTrafficConfPrfCosPriority=_ZxDslTrafficConfPrfCosPriority_Object((1,3,6,1,4,1,3902,1004,42,1,1,7),_ZxDslTrafficConfPrfCosPriority_Type())
zxDslTrafficConfPrfCosPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficConfPrfCosPriority.setStatus(_A)
class _ZxDslTrafficConfPrfDiscardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noDistinction',1),('lowPriorityFirst',2)))
_ZxDslTrafficConfPrfDiscardMode_Type.__name__=_C
_ZxDslTrafficConfPrfDiscardMode_Object=MibTableColumn
zxDslTrafficConfPrfDiscardMode=_ZxDslTrafficConfPrfDiscardMode_Object((1,3,6,1,4,1,3902,1004,42,1,1,8),_ZxDslTrafficConfPrfDiscardMode_Type())
zxDslTrafficConfPrfDiscardMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficConfPrfDiscardMode.setStatus(_A)
_ZxDslTrafficConfPrfRowStatus_Type=RowStatus
_ZxDslTrafficConfPrfRowStatus_Object=MibTableColumn
zxDslTrafficConfPrfRowStatus=_ZxDslTrafficConfPrfRowStatus_Object((1,3,6,1,4,1,3902,1004,42,1,1,30),_ZxDslTrafficConfPrfRowStatus_Type())
zxDslTrafficConfPrfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficConfPrfRowStatus.setStatus(_A)
_ZxDslTrafficInterfaceTable_Object=MibTable
zxDslTrafficInterfaceTable=_ZxDslTrafficInterfaceTable_Object((1,3,6,1,4,1,3902,1004,42,2))
if mibBuilder.loadTexts:zxDslTrafficInterfaceTable.setStatus(_A)
_ZxDslTrafficInterfaceEntry_Object=MibTableRow
zxDslTrafficInterfaceEntry=_ZxDslTrafficInterfaceEntry_Object((1,3,6,1,4,1,3902,1004,42,2,1))
zxDslTrafficInterfaceEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:zxDslTrafficInterfaceEntry.setStatus(_A)
_ZxDslTrafficPort_Type=Integer32
_ZxDslTrafficPort_Object=MibTableColumn
zxDslTrafficPort=_ZxDslTrafficPort_Object((1,3,6,1,4,1,3902,1004,42,2,1,1),_ZxDslTrafficPort_Type())
zxDslTrafficPort.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslTrafficPort.setStatus(_A)
_ZxDslTrafficSvcIface_Type=Integer32
_ZxDslTrafficSvcIface_Object=MibTableColumn
zxDslTrafficSvcIface=_ZxDslTrafficSvcIface_Object((1,3,6,1,4,1,3902,1004,42,2,1,2),_ZxDslTrafficSvcIface_Type())
zxDslTrafficSvcIface.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslTrafficSvcIface.setStatus(_A)
class _ZxDslTrafficSvcIfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pvc',1),('vlan',2)))
_ZxDslTrafficSvcIfaceType_Type.__name__=_C
_ZxDslTrafficSvcIfaceType_Object=MibTableColumn
zxDslTrafficSvcIfaceType=_ZxDslTrafficSvcIfaceType_Object((1,3,6,1,4,1,3902,1004,42,2,1,3),_ZxDslTrafficSvcIfaceType_Type())
zxDslTrafficSvcIfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficSvcIfaceType.setStatus(_A)
class _ZxDslTrafficSvcEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pppoe',1),('ipoe',2),('all',3)))
_ZxDslTrafficSvcEncapType_Type.__name__=_C
_ZxDslTrafficSvcEncapType_Object=MibTableColumn
zxDslTrafficSvcEncapType=_ZxDslTrafficSvcEncapType_Object((1,3,6,1,4,1,3902,1004,42,2,1,4),_ZxDslTrafficSvcEncapType_Type())
zxDslTrafficSvcEncapType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficSvcEncapType.setStatus(_A)
_ZxDslTrafficIfaceEgressPrf_Type=DisplayString
_ZxDslTrafficIfaceEgressPrf_Object=MibTableColumn
zxDslTrafficIfaceEgressPrf=_ZxDslTrafficIfaceEgressPrf_Object((1,3,6,1,4,1,3902,1004,42,2,1,5),_ZxDslTrafficIfaceEgressPrf_Type())
zxDslTrafficIfaceEgressPrf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficIfaceEgressPrf.setStatus(_A)
_ZxDslTrafficIfaceIngressPrf_Type=DisplayString
_ZxDslTrafficIfaceIngressPrf_Object=MibTableColumn
zxDslTrafficIfaceIngressPrf=_ZxDslTrafficIfaceIngressPrf_Object((1,3,6,1,4,1,3902,1004,42,2,1,6),_ZxDslTrafficIfaceIngressPrf_Type())
zxDslTrafficIfaceIngressPrf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficIfaceIngressPrf.setStatus(_A)
_ZxDslTrafficIfaceRowStatus_Type=RowStatus
_ZxDslTrafficIfaceRowStatus_Object=MibTableColumn
zxDslTrafficIfaceRowStatus=_ZxDslTrafficIfaceRowStatus_Object((1,3,6,1,4,1,3902,1004,42,2,1,20),_ZxDslTrafficIfaceRowStatus_Type())
zxDslTrafficIfaceRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficIfaceRowStatus.setStatus(_A)
_ZxDslTrafficIfTable_Object=MibTable
zxDslTrafficIfTable=_ZxDslTrafficIfTable_Object((1,3,6,1,4,1,3902,1004,42,3))
if mibBuilder.loadTexts:zxDslTrafficIfTable.setStatus(_A)
_ZxDslTrafficIfEntry_Object=MibTableRow
zxDslTrafficIfEntry=_ZxDslTrafficIfEntry_Object((1,3,6,1,4,1,3902,1004,42,3,1))
zxDslTrafficIfEntry.setIndexNames((0,_D,_K),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:zxDslTrafficIfEntry.setStatus(_A)
_ZxDslTrafficIfIndex_Type=Integer32
_ZxDslTrafficIfIndex_Object=MibTableColumn
zxDslTrafficIfIndex=_ZxDslTrafficIfIndex_Object((1,3,6,1,4,1,3902,1004,42,3,1,1),_ZxDslTrafficIfIndex_Type())
zxDslTrafficIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslTrafficIfIndex.setStatus(_A)
class _ZxDslTrafficIfCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridgePort',1),('vlan',2)))
_ZxDslTrafficIfCircuitType_Type.__name__=_C
_ZxDslTrafficIfCircuitType_Object=MibTableColumn
zxDslTrafficIfCircuitType=_ZxDslTrafficIfCircuitType_Object((1,3,6,1,4,1,3902,1004,42,3,1,2),_ZxDslTrafficIfCircuitType_Type())
zxDslTrafficIfCircuitType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslTrafficIfCircuitType.setStatus(_A)
_ZxDslTrafficIfLogicalId_Type=Integer32
_ZxDslTrafficIfLogicalId_Object=MibTableColumn
zxDslTrafficIfLogicalId=_ZxDslTrafficIfLogicalId_Object((1,3,6,1,4,1,3902,1004,42,3,1,3),_ZxDslTrafficIfLogicalId_Type())
zxDslTrafficIfLogicalId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslTrafficIfLogicalId.setStatus(_A)
class _ZxDslTrafficIfEthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('pppoe',2),('ipoe',3)))
_ZxDslTrafficIfEthType_Type.__name__=_C
_ZxDslTrafficIfEthType_Object=MibTableColumn
zxDslTrafficIfEthType=_ZxDslTrafficIfEthType_Object((1,3,6,1,4,1,3902,1004,42,3,1,4),_ZxDslTrafficIfEthType_Type())
zxDslTrafficIfEthType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficIfEthType.setStatus(_A)
class _ZxDslTrafficIfEgressPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxDslTrafficIfEgressPrf_Type.__name__=_F
_ZxDslTrafficIfEgressPrf_Object=MibTableColumn
zxDslTrafficIfEgressPrf=_ZxDslTrafficIfEgressPrf_Object((1,3,6,1,4,1,3902,1004,42,3,1,5),_ZxDslTrafficIfEgressPrf_Type())
zxDslTrafficIfEgressPrf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficIfEgressPrf.setStatus(_A)
class _ZxDslTrafficIfIngressPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxDslTrafficIfIngressPrf_Type.__name__=_F
_ZxDslTrafficIfIngressPrf_Object=MibTableColumn
zxDslTrafficIfIngressPrf=_ZxDslTrafficIfIngressPrf_Object((1,3,6,1,4,1,3902,1004,42,3,1,6),_ZxDslTrafficIfIngressPrf_Type())
zxDslTrafficIfIngressPrf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficIfIngressPrf.setStatus(_A)
_ZxDslTrafficIfRowStatus_Type=RowStatus
_ZxDslTrafficIfRowStatus_Object=MibTableColumn
zxDslTrafficIfRowStatus=_ZxDslTrafficIfRowStatus_Object((1,3,6,1,4,1,3902,1004,42,3,1,50),_ZxDslTrafficIfRowStatus_Type())
zxDslTrafficIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslTrafficIfRowStatus.setStatus(_A)
_ZxDslTrafficMgmtGlobalObjects_ObjectIdentity=ObjectIdentity
zxDslTrafficMgmtGlobalObjects=_ZxDslTrafficMgmtGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,42,50))
class _ZxDslTrafficMgmtCapabilities_Type(Bits):namedValues=NamedValues(('supportZxDslTrafficIfTable',0))
_ZxDslTrafficMgmtCapabilities_Type.__name__='Bits'
_ZxDslTrafficMgmtCapabilities_Object=MibScalar
zxDslTrafficMgmtCapabilities=_ZxDslTrafficMgmtCapabilities_Object((1,3,6,1,4,1,3902,1004,42,50,1),_ZxDslTrafficMgmtCapabilities_Type())
zxDslTrafficMgmtCapabilities.setMaxAccess('read-only')
if mibBuilder.loadTexts:zxDslTrafficMgmtCapabilities.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zte':zte,'zxDsl':zxDsl,'zxDslTrafficMgmt':zxDslTrafficMgmt,'zxDslTrafficConfProfileTable':zxDslTrafficConfProfileTable,'zxDslTrafficConfProfileEntry':zxDslTrafficConfProfileEntry,_G:zxDslTrafficConfPrfName,'zxDslTrafficConfPrfCir':zxDslTrafficConfPrfCir,'zxDslTrafficConfPrfCbs':zxDslTrafficConfPrfCbs,'zxDslTrafficConfPrfPir':zxDslTrafficConfPrfPir,'zxDslTrafficConfPrfPbs':zxDslTrafficConfPrfPbs,'zxDslTrafficConfPrfCosPriTrust':zxDslTrafficConfPrfCosPriTrust,'zxDslTrafficConfPrfCosPriority':zxDslTrafficConfPrfCosPriority,'zxDslTrafficConfPrfDiscardMode':zxDslTrafficConfPrfDiscardMode,'zxDslTrafficConfPrfRowStatus':zxDslTrafficConfPrfRowStatus,'zxDslTrafficInterfaceTable':zxDslTrafficInterfaceTable,'zxDslTrafficInterfaceEntry':zxDslTrafficInterfaceEntry,_I:zxDslTrafficPort,_J:zxDslTrafficSvcIface,'zxDslTrafficSvcIfaceType':zxDslTrafficSvcIfaceType,'zxDslTrafficSvcEncapType':zxDslTrafficSvcEncapType,'zxDslTrafficIfaceEgressPrf':zxDslTrafficIfaceEgressPrf,'zxDslTrafficIfaceIngressPrf':zxDslTrafficIfaceIngressPrf,'zxDslTrafficIfaceRowStatus':zxDslTrafficIfaceRowStatus,'zxDslTrafficIfTable':zxDslTrafficIfTable,'zxDslTrafficIfEntry':zxDslTrafficIfEntry,_K:zxDslTrafficIfIndex,_L:zxDslTrafficIfCircuitType,_M:zxDslTrafficIfLogicalId,'zxDslTrafficIfEthType':zxDslTrafficIfEthType,'zxDslTrafficIfEgressPrf':zxDslTrafficIfEgressPrf,'zxDslTrafficIfIngressPrf':zxDslTrafficIfIngressPrf,'zxDslTrafficIfRowStatus':zxDslTrafficIfRowStatus,'zxDslTrafficMgmtGlobalObjects':zxDslTrafficMgmtGlobalObjects,'zxDslTrafficMgmtCapabilities':zxDslTrafficMgmtCapabilities})