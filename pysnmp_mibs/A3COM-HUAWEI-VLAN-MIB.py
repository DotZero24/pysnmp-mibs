_J='vLANMibSubIfPortIndex'
_I='vLANMIbVID'
_H='vLANMibRouterVID'
_G='write-only'
_F='vLANMibRouterPort'
_E='read-write'
_D='A3COM-HUAWEI-VLAN-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hwInternetProtocol,hwLocal,vrpProtocol=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','hwInternetProtocol','hwLocal','vrpProtocol')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Huawei_vlan_ObjectIdentity=ObjectIdentity
huawei_vlan=_Huawei_vlan_ObjectIdentity((1,3,6,1,4,1,43,45,1,1,3,3,3))
_VLANMibRoutertCountTable_Object=MibTable
vLANMibRoutertCountTable=_VLANMibRoutertCountTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,1))
if mibBuilder.loadTexts:vLANMibRoutertCountTable.setStatus(_A)
_VLANMibRoutertCountEntry_Object=MibTableRow
vLANMibRoutertCountEntry=_VLANMibRoutertCountEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,1,1))
vLANMibRoutertCountEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:vLANMibRoutertCountEntry.setStatus(_A)
_VLANMibRouterPort_Type=Integer32
_VLANMibRouterPort_Object=MibTableColumn
vLANMibRouterPort=_VLANMibRouterPort_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,1,1,1),_VLANMibRouterPort_Type())
vLANMibRouterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:vLANMibRouterPort.setStatus(_A)
_VLANMibRouterPortPktDisc_Type=Counter32
_VLANMibRouterPortPktDisc_Object=MibTableColumn
vLANMibRouterPortPktDisc=_VLANMibRouterPortPktDisc_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,1,1,2),_VLANMibRouterPortPktDisc_Type())
vLANMibRouterPortPktDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:vLANMibRouterPortPktDisc.setStatus(_A)
_VLANMibRouterPortPktTran_Type=Counter32
_VLANMibRouterPortPktTran_Object=MibTableColumn
vLANMibRouterPortPktTran=_VLANMibRouterPortPktTran_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,1,1,3),_VLANMibRouterPortPktTran_Type())
vLANMibRouterPortPktTran.setMaxAccess(_B)
if mibBuilder.loadTexts:vLANMibRouterPortPktTran.setStatus(_A)
class _VLANMibClearRouterStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_VLANMibClearRouterStatistics_Type.__name__=_C
_VLANMibClearRouterStatistics_Object=MibTableColumn
vLANMibClearRouterStatistics=_VLANMibClearRouterStatistics_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,1,1,4),_VLANMibClearRouterStatistics_Type())
vLANMibClearRouterStatistics.setMaxAccess(_G)
if mibBuilder.loadTexts:vLANMibClearRouterStatistics.setStatus(_A)
_VLANMibRoutertVlanCountTable_Object=MibTable
vLANMibRoutertVlanCountTable=_VLANMibRoutertVlanCountTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,2))
if mibBuilder.loadTexts:vLANMibRoutertVlanCountTable.setStatus(_A)
_VLANMibRoutertVlanCountEntry_Object=MibTableRow
vLANMibRoutertVlanCountEntry=_VLANMibRoutertVlanCountEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,2,1))
vLANMibRoutertVlanCountEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:vLANMibRoutertVlanCountEntry.setStatus(_A)
class _VLANMibRouterVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VLANMibRouterVID_Type.__name__=_C
_VLANMibRouterVID_Object=MibTableColumn
vLANMibRouterVID=_VLANMibRouterVID_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,2,1,1),_VLANMibRouterVID_Type())
vLANMibRouterVID.setMaxAccess(_B)
if mibBuilder.loadTexts:vLANMibRouterVID.setStatus(_A)
_VLANMibRouterVlanPacketTran_Type=Counter32
_VLANMibRouterVlanPacketTran_Object=MibTableColumn
vLANMibRouterVlanPacketTran=_VLANMibRouterVlanPacketTran_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,2,1,2),_VLANMibRouterVlanPacketTran_Type())
vLANMibRouterVlanPacketTran.setMaxAccess(_B)
if mibBuilder.loadTexts:vLANMibRouterVlanPacketTran.setStatus(_A)
_VLANMibRouterVlanPacketSent_Type=Counter32
_VLANMibRouterVlanPacketSent_Object=MibTableColumn
vLANMibRouterVlanPacketSent=_VLANMibRouterVlanPacketSent_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,2,1,3),_VLANMibRouterVlanPacketSent_Type())
vLANMibRouterVlanPacketSent.setMaxAccess(_B)
if mibBuilder.loadTexts:vLANMibRouterVlanPacketSent.setStatus(_A)
class _VLANMibClearVidStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_VLANMibClearVidStatistics_Type.__name__=_C
_VLANMibClearVidStatistics_Object=MibTableColumn
vLANMibClearVidStatistics=_VLANMibClearVidStatistics_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,2,1,4),_VLANMibClearVidStatistics_Type())
vLANMibClearVidStatistics.setMaxAccess(_G)
if mibBuilder.loadTexts:vLANMibClearVidStatistics.setStatus(_A)
_VLANMibRouterMaxPkTable_Object=MibTable
vLANMibRouterMaxPkTable=_VLANMibRouterMaxPkTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,9))
if mibBuilder.loadTexts:vLANMibRouterMaxPkTable.setStatus(_A)
_VLANMibRouterMaxPkEntry_Object=MibTableRow
vLANMibRouterMaxPkEntry=_VLANMibRouterMaxPkEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,9,1))
vLANMibRouterMaxPkEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:vLANMibRouterMaxPkEntry.setStatus(_A)
class _VLANMIbVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VLANMIbVID_Type.__name__=_C
_VLANMIbVID_Object=MibTableColumn
vLANMIbVID=_VLANMIbVID_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,9,1,1),_VLANMIbVID_Type())
vLANMIbVID.setMaxAccess(_B)
if mibBuilder.loadTexts:vLANMIbVID.setStatus(_A)
_VLANMibRouterMaxPktProcessCount_Type=Unsigned32
_VLANMibRouterMaxPktProcessCount_Object=MibTableColumn
vLANMibRouterMaxPktProcessCount=_VLANMibRouterMaxPktProcessCount_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,9,1,2),_VLANMibRouterMaxPktProcessCount_Type())
vLANMibRouterMaxPktProcessCount.setMaxAccess(_E)
if mibBuilder.loadTexts:vLANMibRouterMaxPktProcessCount.setStatus(_A)
_VLANMibSubIfTable_Object=MibTable
vLANMibSubIfTable=_VLANMibSubIfTable_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,11))
if mibBuilder.loadTexts:vLANMibSubIfTable.setStatus(_A)
_VLANMibSubIfEntry_Object=MibTableRow
vLANMibSubIfEntry=_VLANMibSubIfEntry_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,11,1))
vLANMibSubIfEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:vLANMibSubIfEntry.setStatus(_A)
_VLANMibSubIfPortIndex_Type=Integer32
_VLANMibSubIfPortIndex_Object=MibTableColumn
vLANMibSubIfPortIndex=_VLANMibSubIfPortIndex_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,11,1,1),_VLANMibSubIfPortIndex_Type())
vLANMibSubIfPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vLANMibSubIfPortIndex.setStatus(_A)
class _VLANMibSubIfEncapsulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('iSL',1),('dot1q',2)))
_VLANMibSubIfEncapsulation_Type.__name__=_C
_VLANMibSubIfEncapsulation_Object=MibTableColumn
vLANMibSubIfEncapsulation=_VLANMibSubIfEncapsulation_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,11,1,2),_VLANMibSubIfEncapsulation_Type())
vLANMibSubIfEncapsulation.setMaxAccess(_E)
if mibBuilder.loadTexts:vLANMibSubIfEncapsulation.setStatus(_A)
class _VLANMibSubIfVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VLANMibSubIfVID_Type.__name__=_C
_VLANMibSubIfVID_Object=MibTableColumn
vLANMibSubIfVID=_VLANMibSubIfVID_Object((1,3,6,1,4,1,43,45,1,1,3,3,3,11,1,3),_VLANMibSubIfVID_Type())
vLANMibSubIfVID.setMaxAccess(_E)
if mibBuilder.loadTexts:vLANMibSubIfVID.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'huawei-vlan':huawei_vlan,'vLANMibRoutertCountTable':vLANMibRoutertCountTable,'vLANMibRoutertCountEntry':vLANMibRoutertCountEntry,_F:vLANMibRouterPort,'vLANMibRouterPortPktDisc':vLANMibRouterPortPktDisc,'vLANMibRouterPortPktTran':vLANMibRouterPortPktTran,'vLANMibClearRouterStatistics':vLANMibClearRouterStatistics,'vLANMibRoutertVlanCountTable':vLANMibRoutertVlanCountTable,'vLANMibRoutertVlanCountEntry':vLANMibRoutertVlanCountEntry,_H:vLANMibRouterVID,'vLANMibRouterVlanPacketTran':vLANMibRouterVlanPacketTran,'vLANMibRouterVlanPacketSent':vLANMibRouterVlanPacketSent,'vLANMibClearVidStatistics':vLANMibClearVidStatistics,'vLANMibRouterMaxPkTable':vLANMibRouterMaxPkTable,'vLANMibRouterMaxPkEntry':vLANMibRouterMaxPkEntry,_I:vLANMIbVID,'vLANMibRouterMaxPktProcessCount':vLANMibRouterMaxPktProcessCount,'vLANMibSubIfTable':vLANMibSubIfTable,'vLANMibSubIfEntry':vLANMibSubIfEntry,_J:vLANMibSubIfPortIndex,'vLANMibSubIfEncapsulation':vLANMibSubIfEncapsulation,'vLANMibSubIfVID':vLANMibSubIfVID})