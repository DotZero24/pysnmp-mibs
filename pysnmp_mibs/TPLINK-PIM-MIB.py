_R='tpPimRPAddress'
_Q='tpPimRPGroupAddress'
_P='tpPimCRPSetInterfaceIndex'
_O='tpPimNeighborAddress'
_N='sparse'
_M='routeport'
_L='loopback'
_K='tpPimInterfaceIndex'
_J='enable'
_I='disable'
_H='seconds'
_G='OctetString'
_F='TPLINK-PIM-MIB'
_E='deprecated'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkPimMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,77))
if mibBuilder.loadTexts:tplinkPimMIB.setRevisions(('2012-12-13 09:30',))
_TplinkPimMIBObjects_ObjectIdentity=ObjectIdentity
tplinkPimMIBObjects=_TplinkPimMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,77,1))
_TpPim_ObjectIdentity=ObjectIdentity
tpPim=_TpPim_ObjectIdentity((1,3,6,1,4,1,11863,6,77,1,1))
class _TpSGExpiryTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,65535))
_TpSGExpiryTimer_Type.__name__=_C
_TpSGExpiryTimer_Object=MibScalar
tpSGExpiryTimer=_TpSGExpiryTimer_Object((1,3,6,1,4,1,11863,6,77,1,1,1),_TpSGExpiryTimer_Type())
tpSGExpiryTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSGExpiryTimer.setStatus(_A)
if mibBuilder.loadTexts:tpSGExpiryTimer.setUnits(_H)
class _TpPimdataThresholdRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('zero',0),('infinity',1)))
_TpPimdataThresholdRate_Type.__name__=_C
_TpPimdataThresholdRate_Object=MibScalar
tpPimdataThresholdRate=_TpPimdataThresholdRate_Object((1,3,6,1,4,1,11863,6,77,1,1,2),_TpPimdataThresholdRate_Type())
tpPimdataThresholdRate.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimdataThresholdRate.setStatus(_A)
if mibBuilder.loadTexts:tpPimdataThresholdRate.setUnits(_H)
_TpPimInterfaceTable_Object=MibTable
tpPimInterfaceTable=_TpPimInterfaceTable_Object((1,3,6,1,4,1,11863,6,77,1,1,3))
if mibBuilder.loadTexts:tpPimInterfaceTable.setStatus(_A)
_TpPimInterfaceEntry_Object=MibTableRow
tpPimInterfaceEntry=_TpPimInterfaceEntry_Object((1,3,6,1,4,1,11863,6,77,1,1,3,1))
tpPimInterfaceEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:tpPimInterfaceEntry.setStatus(_A)
class _TpPimInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_TpPimInterface_Type.__name__=_G
_TpPimInterface_Object=MibTableColumn
tpPimInterface=_TpPimInterface_Object((1,3,6,1,4,1,11863,6,77,1,1,3,1,1),_TpPimInterface_Type())
tpPimInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimInterface.setStatus(_A)
_TpPimInterfaceIndex_Type=Integer32
_TpPimInterfaceIndex_Object=MibTableColumn
tpPimInterfaceIndex=_TpPimInterfaceIndex_Object((1,3,6,1,4,1,11863,6,77,1,1,3,1,2),_TpPimInterfaceIndex_Type())
tpPimInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimInterfaceIndex.setStatus(_A)
class _TpPimInterfaceType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('vlan',0),(_L,1),(_M,2)))
_TpPimInterfaceType_Type.__name__=_C
_TpPimInterfaceType_Object=MibTableColumn
tpPimInterfaceType=_TpPimInterfaceType_Object((1,3,6,1,4,1,11863,6,77,1,1,3,1,3),_TpPimInterfaceType_Type())
tpPimInterfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimInterfaceType.setStatus(_A)
_TpPimInterfaceAddress_Type=IpAddress
_TpPimInterfaceAddress_Object=MibTableColumn
tpPimInterfaceAddress=_TpPimInterfaceAddress_Object((1,3,6,1,4,1,11863,6,77,1,1,3,1,4),_TpPimInterfaceAddress_Type())
tpPimInterfaceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimInterfaceAddress.setStatus(_A)
_TpPimInterfaceNetMask_Type=IpAddress
_TpPimInterfaceNetMask_Object=MibTableColumn
tpPimInterfaceNetMask=_TpPimInterfaceNetMask_Object((1,3,6,1,4,1,11863,6,77,1,1,3,1,5),_TpPimInterfaceNetMask_Type())
tpPimInterfaceNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimInterfaceNetMask.setStatus(_A)
class _TpPimInterfaceMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('dense',1),(_N,2)))
_TpPimInterfaceMode_Type.__name__=_C
_TpPimInterfaceMode_Object=MibTableColumn
tpPimInterfaceMode=_TpPimInterfaceMode_Object((1,3,6,1,4,1,11863,6,77,1,1,3,1,6),_TpPimInterfaceMode_Type())
tpPimInterfaceMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimInterfaceMode.setStatus(_A)
class _TpPimInterfaceDRPriority_Type(Integer32):defaultValue=1
_TpPimInterfaceDRPriority_Type.__name__=_C
_TpPimInterfaceDRPriority_Object=MibTableColumn
tpPimInterfaceDRPriority=_TpPimInterfaceDRPriority_Object((1,3,6,1,4,1,11863,6,77,1,1,3,1,7),_TpPimInterfaceDRPriority_Type())
tpPimInterfaceDRPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimInterfaceDRPriority.setStatus(_A)
_TpPimInterfaceDRAddress_Type=IpAddress
_TpPimInterfaceDRAddress_Object=MibTableColumn
tpPimInterfaceDRAddress=_TpPimInterfaceDRAddress_Object((1,3,6,1,4,1,11863,6,77,1,1,3,1,8),_TpPimInterfaceDRAddress_Type())
tpPimInterfaceDRAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimInterfaceDRAddress.setStatus(_A)
class _TpPimInterfaceHelloInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18725))
_TpPimInterfaceHelloInterval_Type.__name__=_C
_TpPimInterfaceHelloInterval_Object=MibTableColumn
tpPimInterfaceHelloInterval=_TpPimInterfaceHelloInterval_Object((1,3,6,1,4,1,11863,6,77,1,1,3,1,9),_TpPimInterfaceHelloInterval_Type())
tpPimInterfaceHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimInterfaceHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:tpPimInterfaceHelloInterval.setUnits(_H)
class _TpPimInterfaceBsrBorder_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_TpPimInterfaceBsrBorder_Type.__name__=_C
_TpPimInterfaceBsrBorder_Object=MibTableColumn
tpPimInterfaceBsrBorder=_TpPimInterfaceBsrBorder_Object((1,3,6,1,4,1,11863,6,77,1,1,3,1,10),_TpPimInterfaceBsrBorder_Type())
tpPimInterfaceBsrBorder.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimInterfaceBsrBorder.setStatus(_A)
class _TpPimInterfaceJoinPruneInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18724))
_TpPimInterfaceJoinPruneInterval_Type.__name__=_C
_TpPimInterfaceJoinPruneInterval_Object=MibTableColumn
tpPimInterfaceJoinPruneInterval=_TpPimInterfaceJoinPruneInterval_Object((1,3,6,1,4,1,11863,6,77,1,1,3,1,11),_TpPimInterfaceJoinPruneInterval_Type())
tpPimInterfaceJoinPruneInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimInterfaceJoinPruneInterval.setStatus(_A)
if mibBuilder.loadTexts:tpPimInterfaceJoinPruneInterval.setUnits(_H)
_TpPimNeighborTable_Object=MibTable
tpPimNeighborTable=_TpPimNeighborTable_Object((1,3,6,1,4,1,11863,6,77,1,1,4))
if mibBuilder.loadTexts:tpPimNeighborTable.setStatus(_A)
_TpPimNeighborEntry_Object=MibTableRow
tpPimNeighborEntry=_TpPimNeighborEntry_Object((1,3,6,1,4,1,11863,6,77,1,1,4,1))
tpPimNeighborEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:tpPimNeighborEntry.setStatus(_A)
class _TpPimNeighborInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_TpPimNeighborInterface_Type.__name__=_G
_TpPimNeighborInterface_Object=MibTableColumn
tpPimNeighborInterface=_TpPimNeighborInterface_Object((1,3,6,1,4,1,11863,6,77,1,1,4,1,1),_TpPimNeighborInterface_Type())
tpPimNeighborInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimNeighborInterface.setStatus(_A)
_TpPimNeighborInterfaceIndex_Type=Integer32
_TpPimNeighborInterfaceIndex_Object=MibTableColumn
tpPimNeighborInterfaceIndex=_TpPimNeighborInterfaceIndex_Object((1,3,6,1,4,1,11863,6,77,1,1,4,1,2),_TpPimNeighborInterfaceIndex_Type())
tpPimNeighborInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimNeighborInterfaceIndex.setStatus(_A)
_TpPimNeighborAddress_Type=IpAddress
_TpPimNeighborAddress_Object=MibTableColumn
tpPimNeighborAddress=_TpPimNeighborAddress_Object((1,3,6,1,4,1,11863,6,77,1,1,4,1,3),_TpPimNeighborAddress_Type())
tpPimNeighborAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimNeighborAddress.setStatus(_A)
_TpPimNeighborUpTime_Type=TimeTicks
_TpPimNeighborUpTime_Object=MibTableColumn
tpPimNeighborUpTime=_TpPimNeighborUpTime_Object((1,3,6,1,4,1,11863,6,77,1,1,4,1,4),_TpPimNeighborUpTime_Type())
tpPimNeighborUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimNeighborUpTime.setStatus(_A)
_TpPimNeighborExpiryTime_Type=TimeTicks
_TpPimNeighborExpiryTime_Object=MibTableColumn
tpPimNeighborExpiryTime=_TpPimNeighborExpiryTime_Object((1,3,6,1,4,1,11863,6,77,1,1,4,1,5),_TpPimNeighborExpiryTime_Type())
tpPimNeighborExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimNeighborExpiryTime.setStatus(_A)
class _TpPimNeighborMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dense',1),(_N,2)))
_TpPimNeighborMode_Type.__name__=_C
_TpPimNeighborMode_Object=MibTableColumn
tpPimNeighborMode=_TpPimNeighborMode_Object((1,3,6,1,4,1,11863,6,77,1,1,4,1,6),_TpPimNeighborMode_Type())
tpPimNeighborMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimNeighborMode.setStatus(_E)
_TpPimCandidateBSRSet_ObjectIdentity=ObjectIdentity
tpPimCandidateBSRSet=_TpPimCandidateBSRSet_ObjectIdentity((1,3,6,1,4,1,11863,6,77,1,1,5))
class _TpPimCBSRInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_TpPimCBSRInterface_Type.__name__=_G
_TpPimCBSRInterface_Object=MibScalar
tpPimCBSRInterface=_TpPimCBSRInterface_Object((1,3,6,1,4,1,11863,6,77,1,1,5,1),_TpPimCBSRInterface_Type())
tpPimCBSRInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimCBSRInterface.setStatus(_A)
_TpPimCBSRInterfaceIndex_Type=Integer32
_TpPimCBSRInterfaceIndex_Object=MibScalar
tpPimCBSRInterfaceIndex=_TpPimCBSRInterfaceIndex_Object((1,3,6,1,4,1,11863,6,77,1,1,5,2),_TpPimCBSRInterfaceIndex_Type())
tpPimCBSRInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimCBSRInterfaceIndex.setStatus(_A)
class _TpPimCBSRHashMaskLength_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_TpPimCBSRHashMaskLength_Type.__name__=_C
_TpPimCBSRHashMaskLength_Object=MibScalar
tpPimCBSRHashMaskLength=_TpPimCBSRHashMaskLength_Object((1,3,6,1,4,1,11863,6,77,1,1,5,3),_TpPimCBSRHashMaskLength_Type())
tpPimCBSRHashMaskLength.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimCBSRHashMaskLength.setStatus(_A)
class _TpPimCBSRPriority_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TpPimCBSRPriority_Type.__name__=_C
_TpPimCBSRPriority_Object=MibScalar
tpPimCBSRPriority=_TpPimCBSRPriority_Object((1,3,6,1,4,1,11863,6,77,1,1,5,4),_TpPimCBSRPriority_Type())
tpPimCBSRPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimCBSRPriority.setStatus(_A)
_TpPimStaticRpSet_ObjectIdentity=ObjectIdentity
tpPimStaticRpSet=_TpPimStaticRpSet_ObjectIdentity((1,3,6,1,4,1,11863,6,77,1,1,6))
_TpPimStaticRpAddress_Type=IpAddress
_TpPimStaticRpAddress_Object=MibScalar
tpPimStaticRpAddress=_TpPimStaticRpAddress_Object((1,3,6,1,4,1,11863,6,77,1,1,6,1),_TpPimStaticRpAddress_Type())
tpPimStaticRpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimStaticRpAddress.setStatus(_A)
class _TpPimStaticRpOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_TpPimStaticRpOverride_Type.__name__=_C
_TpPimStaticRpOverride_Object=MibScalar
tpPimStaticRpOverride=_TpPimStaticRpOverride_Object((1,3,6,1,4,1,11863,6,77,1,1,6,2),_TpPimStaticRpOverride_Type())
tpPimStaticRpOverride.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimStaticRpOverride.setStatus(_A)
_TpPimCandidateRPSetTable_Object=MibTable
tpPimCandidateRPSetTable=_TpPimCandidateRPSetTable_Object((1,3,6,1,4,1,11863,6,77,1,1,7))
if mibBuilder.loadTexts:tpPimCandidateRPSetTable.setStatus(_A)
_TpPimCandidateRPSetEntry_Object=MibTableRow
tpPimCandidateRPSetEntry=_TpPimCandidateRPSetEntry_Object((1,3,6,1,4,1,11863,6,77,1,1,7,1))
tpPimCandidateRPSetEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:tpPimCandidateRPSetEntry.setStatus(_A)
class _TpPimCRPSetInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_TpPimCRPSetInterface_Type.__name__=_G
_TpPimCRPSetInterface_Object=MibTableColumn
tpPimCRPSetInterface=_TpPimCRPSetInterface_Object((1,3,6,1,4,1,11863,6,77,1,1,7,1,1),_TpPimCRPSetInterface_Type())
tpPimCRPSetInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimCRPSetInterface.setStatus(_A)
_TpPimCRPSetInterfaceIndex_Type=Integer32
_TpPimCRPSetInterfaceIndex_Object=MibTableColumn
tpPimCRPSetInterfaceIndex=_TpPimCRPSetInterfaceIndex_Object((1,3,6,1,4,1,11863,6,77,1,1,7,1,2),_TpPimCRPSetInterfaceIndex_Type())
tpPimCRPSetInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimCRPSetInterfaceIndex.setStatus(_A)
class _TpPimCRPSetInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('vlan',0),(_L,1),(_M,2)))
_TpPimCRPSetInterfaceType_Type.__name__=_C
_TpPimCRPSetInterfaceType_Object=MibTableColumn
tpPimCRPSetInterfaceType=_TpPimCRPSetInterfaceType_Object((1,3,6,1,4,1,11863,6,77,1,1,7,1,3),_TpPimCRPSetInterfaceType_Type())
tpPimCRPSetInterfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimCRPSetInterfaceType.setStatus(_E)
class _TpPimCRPSetPriority_Type(Integer32):defaultValue=192;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TpPimCRPSetPriority_Type.__name__=_C
_TpPimCRPSetPriority_Object=MibTableColumn
tpPimCRPSetPriority=_TpPimCRPSetPriority_Object((1,3,6,1,4,1,11863,6,77,1,1,7,1,4),_TpPimCRPSetPriority_Type())
tpPimCRPSetPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimCRPSetPriority.setStatus(_A)
class _TpPimCRPSetInterVal_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TpPimCRPSetInterVal_Type.__name__=_C
_TpPimCRPSetInterVal_Object=MibTableColumn
tpPimCRPSetInterVal=_TpPimCRPSetInterVal_Object((1,3,6,1,4,1,11863,6,77,1,1,7,1,5),_TpPimCRPSetInterVal_Type())
tpPimCRPSetInterVal.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimCRPSetInterVal.setStatus(_A)
_TpPimCRPSetNextAdvertisementTime_Type=TimeTicks
_TpPimCRPSetNextAdvertisementTime_Object=MibTableColumn
tpPimCRPSetNextAdvertisementTime=_TpPimCRPSetNextAdvertisementTime_Object((1,3,6,1,4,1,11863,6,77,1,1,7,1,6),_TpPimCRPSetNextAdvertisementTime_Type())
tpPimCRPSetNextAdvertisementTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimCRPSetNextAdvertisementTime.setStatus(_A)
class _TpPimCRPSetInterfaceStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_TpPimCRPSetInterfaceStatus_Type.__name__=_C
_TpPimCRPSetInterfaceStatus_Object=MibTableColumn
tpPimCRPSetInterfaceStatus=_TpPimCRPSetInterfaceStatus_Object((1,3,6,1,4,1,11863,6,77,1,1,7,1,7),_TpPimCRPSetInterfaceStatus_Type())
tpPimCRPSetInterfaceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPimCRPSetInterfaceStatus.setStatus(_E)
_TpPimRPMappingTable_Object=MibTable
tpPimRPMappingTable=_TpPimRPMappingTable_Object((1,3,6,1,4,1,11863,6,77,1,1,8))
if mibBuilder.loadTexts:tpPimRPMappingTable.setStatus(_E)
_TpPimRPMappingEntry_Object=MibTableRow
tpPimRPMappingEntry=_TpPimRPMappingEntry_Object((1,3,6,1,4,1,11863,6,77,1,1,8,1))
tpPimRPMappingEntry.setIndexNames((0,_F,_Q),(0,_F,_R))
if mibBuilder.loadTexts:tpPimRPMappingEntry.setStatus(_E)
_TpPimRPGroupAddress_Type=IpAddress
_TpPimRPGroupAddress_Object=MibTableColumn
tpPimRPGroupAddress=_TpPimRPGroupAddress_Object((1,3,6,1,4,1,11863,6,77,1,1,8,1,1),_TpPimRPGroupAddress_Type())
tpPimRPGroupAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimRPGroupAddress.setStatus(_E)
_TpPimRPAddress_Type=IpAddress
_TpPimRPAddress_Object=MibTableColumn
tpPimRPAddress=_TpPimRPAddress_Object((1,3,6,1,4,1,11863,6,77,1,1,8,1,2),_TpPimRPAddress_Type())
tpPimRPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimRPAddress.setStatus(_E)
_TpPimRPInfoSource_Type=IpAddress
_TpPimRPInfoSource_Object=MibTableColumn
tpPimRPInfoSource=_TpPimRPInfoSource_Object((1,3,6,1,4,1,11863,6,77,1,1,8,1,3),_TpPimRPInfoSource_Type())
tpPimRPInfoSource.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimRPInfoSource.setStatus(_E)
_TpPimRPPriority_Type=Integer32
_TpPimRPPriority_Object=MibTableColumn
tpPimRPPriority=_TpPimRPPriority_Object((1,3,6,1,4,1,11863,6,77,1,1,8,1,4),_TpPimRPPriority_Type())
tpPimRPPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimRPPriority.setStatus(_E)
_TpPimRPHoldTime_Type=TimeTicks
_TpPimRPHoldTime_Object=MibTableColumn
tpPimRPHoldTime=_TpPimRPHoldTime_Object((1,3,6,1,4,1,11863,6,77,1,1,8,1,5),_TpPimRPHoldTime_Type())
tpPimRPHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimRPHoldTime.setStatus(_E)
_TpPimRPExpire_Type=TimeTicks
_TpPimRPExpire_Object=MibTableColumn
tpPimRPExpire=_TpPimRPExpire_Object((1,3,6,1,4,1,11863,6,77,1,1,8,1,6),_TpPimRPExpire_Type())
tpPimRPExpire.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPimRPExpire.setStatus(_E)
_TplinkPimNotifications_ObjectIdentity=ObjectIdentity
tplinkPimNotifications=_TplinkPimNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,77,2))
mibBuilder.exportSymbols(_F,**{'tplinkPimMIB':tplinkPimMIB,'tplinkPimMIBObjects':tplinkPimMIBObjects,'tpPim':tpPim,'tpSGExpiryTimer':tpSGExpiryTimer,'tpPimdataThresholdRate':tpPimdataThresholdRate,'tpPimInterfaceTable':tpPimInterfaceTable,'tpPimInterfaceEntry':tpPimInterfaceEntry,'tpPimInterface':tpPimInterface,_K:tpPimInterfaceIndex,'tpPimInterfaceType':tpPimInterfaceType,'tpPimInterfaceAddress':tpPimInterfaceAddress,'tpPimInterfaceNetMask':tpPimInterfaceNetMask,'tpPimInterfaceMode':tpPimInterfaceMode,'tpPimInterfaceDRPriority':tpPimInterfaceDRPriority,'tpPimInterfaceDRAddress':tpPimInterfaceDRAddress,'tpPimInterfaceHelloInterval':tpPimInterfaceHelloInterval,'tpPimInterfaceBsrBorder':tpPimInterfaceBsrBorder,'tpPimInterfaceJoinPruneInterval':tpPimInterfaceJoinPruneInterval,'tpPimNeighborTable':tpPimNeighborTable,'tpPimNeighborEntry':tpPimNeighborEntry,'tpPimNeighborInterface':tpPimNeighborInterface,'tpPimNeighborInterfaceIndex':tpPimNeighborInterfaceIndex,_O:tpPimNeighborAddress,'tpPimNeighborUpTime':tpPimNeighborUpTime,'tpPimNeighborExpiryTime':tpPimNeighborExpiryTime,'tpPimNeighborMode':tpPimNeighborMode,'tpPimCandidateBSRSet':tpPimCandidateBSRSet,'tpPimCBSRInterface':tpPimCBSRInterface,'tpPimCBSRInterfaceIndex':tpPimCBSRInterfaceIndex,'tpPimCBSRHashMaskLength':tpPimCBSRHashMaskLength,'tpPimCBSRPriority':tpPimCBSRPriority,'tpPimStaticRpSet':tpPimStaticRpSet,'tpPimStaticRpAddress':tpPimStaticRpAddress,'tpPimStaticRpOverride':tpPimStaticRpOverride,'tpPimCandidateRPSetTable':tpPimCandidateRPSetTable,'tpPimCandidateRPSetEntry':tpPimCandidateRPSetEntry,'tpPimCRPSetInterface':tpPimCRPSetInterface,_P:tpPimCRPSetInterfaceIndex,'tpPimCRPSetInterfaceType':tpPimCRPSetInterfaceType,'tpPimCRPSetPriority':tpPimCRPSetPriority,'tpPimCRPSetInterVal':tpPimCRPSetInterVal,'tpPimCRPSetNextAdvertisementTime':tpPimCRPSetNextAdvertisementTime,'tpPimCRPSetInterfaceStatus':tpPimCRPSetInterfaceStatus,'tpPimRPMappingTable':tpPimRPMappingTable,'tpPimRPMappingEntry':tpPimRPMappingEntry,_Q:tpPimRPGroupAddress,_R:tpPimRPAddress,'tpPimRPInfoSource':tpPimRPInfoSource,'tpPimRPPriority':tpPimRPPriority,'tpPimRPHoldTime':tpPimRPHoldTime,'tpPimRPExpire':tpPimRPExpire,'tplinkPimNotifications':tplinkPimNotifications})