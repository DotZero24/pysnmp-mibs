_e='arubaWiredDSSIfTableGroup'
_d='arubaWiredDSMStatusTableGroup'
_c='arubaWiredDSSIfOutBroadcastPkts'
_b='arubaWiredDSSIfOutMulticastPkts'
_a='arubaWiredDSSIfOutErrors'
_Z='arubaWiredDSSIfOutDiscards'
_Y='arubaWiredDSSIfOutUcastPkts'
_X='arubaWiredDSSIfOutOctets'
_W='arubaWiredDSSIfInBroadcastPkts'
_V='arubaWiredDSSIfInMulticastPkts'
_U='arubaWiredDSSIfInUnknownProtos'
_T='arubaWiredDSSIfInErrors'
_S='arubaWiredDSSIfInDiscards'
_R='arubaWiredDSSIfInUcastPkts'
_Q='arubaWiredDSSIfInOctets'
_P='arubaWiredDSSIfDescr'
_O='arubaWiredDSMOperStatus'
_N='arubaWiredDSMPhysAddress'
_M='arubaWiredDSMProductNum'
_L='arubaWiredDSMSerialNum'
_K='arubaWiredDSMDescr'
_J='arubaWiredDSMName'
_I='arubaWiredDSSIfIndex'
_H='arubaWiredDSSModuleIndex'
_G='arubaWiredDSMIndex'
_F='not-accessible'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='ARUBAWIRED-DIST-SERVICES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','TextualConvention')
arubaWiredDistServicesMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,25))
if mibBuilder.loadTexts:arubaWiredDistServicesMIB.setRevisions(('2022-01-31 00:00',))
_ArubaWiredDSMStatus_ObjectIdentity=ObjectIdentity
arubaWiredDSMStatus=_ArubaWiredDSMStatus_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,25,1))
_ArubaWiredDSMStatusTable_Object=MibTable
arubaWiredDSMStatusTable=_ArubaWiredDSMStatusTable_Object((1,3,6,1,4,1,47196,4,1,1,3,25,1,1))
if mibBuilder.loadTexts:arubaWiredDSMStatusTable.setStatus(_A)
_ArubaWiredDSMStatusEntry_Object=MibTableRow
arubaWiredDSMStatusEntry=_ArubaWiredDSMStatusEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,25,1,1,1))
arubaWiredDSMStatusEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:arubaWiredDSMStatusEntry.setStatus(_A)
_ArubaWiredDSMIndex_Type=Unsigned32
_ArubaWiredDSMIndex_Object=MibTableColumn
arubaWiredDSMIndex=_ArubaWiredDSMIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,25,1,1,1,1),_ArubaWiredDSMIndex_Type())
arubaWiredDSMIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredDSMIndex.setStatus(_A)
class _ArubaWiredDSMName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredDSMName_Type.__name__=_D
_ArubaWiredDSMName_Object=MibTableColumn
arubaWiredDSMName=_ArubaWiredDSMName_Object((1,3,6,1,4,1,47196,4,1,1,3,25,1,1,1,2),_ArubaWiredDSMName_Type())
arubaWiredDSMName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSMName.setStatus(_A)
class _ArubaWiredDSMDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_ArubaWiredDSMDescr_Type.__name__=_D
_ArubaWiredDSMDescr_Object=MibTableColumn
arubaWiredDSMDescr=_ArubaWiredDSMDescr_Object((1,3,6,1,4,1,47196,4,1,1,3,25,1,1,1,3),_ArubaWiredDSMDescr_Type())
arubaWiredDSMDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSMDescr.setStatus(_A)
class _ArubaWiredDSMSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredDSMSerialNum_Type.__name__=_D
_ArubaWiredDSMSerialNum_Object=MibTableColumn
arubaWiredDSMSerialNum=_ArubaWiredDSMSerialNum_Object((1,3,6,1,4,1,47196,4,1,1,3,25,1,1,1,4),_ArubaWiredDSMSerialNum_Type())
arubaWiredDSMSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSMSerialNum.setStatus(_A)
class _ArubaWiredDSMProductNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredDSMProductNum_Type.__name__=_D
_ArubaWiredDSMProductNum_Object=MibTableColumn
arubaWiredDSMProductNum=_ArubaWiredDSMProductNum_Object((1,3,6,1,4,1,47196,4,1,1,3,25,1,1,1,5),_ArubaWiredDSMProductNum_Type())
arubaWiredDSMProductNum.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSMProductNum.setStatus(_A)
_ArubaWiredDSMPhysAddress_Type=MacAddress
_ArubaWiredDSMPhysAddress_Object=MibTableColumn
arubaWiredDSMPhysAddress=_ArubaWiredDSMPhysAddress_Object((1,3,6,1,4,1,47196,4,1,1,3,25,1,1,1,6),_ArubaWiredDSMPhysAddress_Type())
arubaWiredDSMPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSMPhysAddress.setStatus(_A)
class _ArubaWiredDSMOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initializing',1),('ready',2),('failed',3)))
_ArubaWiredDSMOperStatus_Type.__name__=_E
_ArubaWiredDSMOperStatus_Object=MibTableColumn
arubaWiredDSMOperStatus=_ArubaWiredDSMOperStatus_Object((1,3,6,1,4,1,47196,4,1,1,3,25,1,1,1,7),_ArubaWiredDSMOperStatus_Type())
arubaWiredDSMOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSMOperStatus.setStatus(_A)
_ArubaWiredDSSInterfaces_ObjectIdentity=ObjectIdentity
arubaWiredDSSInterfaces=_ArubaWiredDSSInterfaces_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,25,2))
_ArubaWiredDSSIfTable_Object=MibTable
arubaWiredDSSIfTable=_ArubaWiredDSSIfTable_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1))
if mibBuilder.loadTexts:arubaWiredDSSIfTable.setStatus(_A)
_ArubaWiredDSSIfEntry_Object=MibTableRow
arubaWiredDSSIfEntry=_ArubaWiredDSSIfEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1))
arubaWiredDSSIfEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:arubaWiredDSSIfEntry.setStatus(_A)
class _ArubaWiredDSSModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredDSSModuleIndex_Type.__name__=_E
_ArubaWiredDSSModuleIndex_Object=MibTableColumn
arubaWiredDSSModuleIndex=_ArubaWiredDSSModuleIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,1),_ArubaWiredDSSModuleIndex_Type())
arubaWiredDSSModuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredDSSModuleIndex.setStatus(_A)
class _ArubaWiredDSSIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredDSSIfIndex_Type.__name__=_E
_ArubaWiredDSSIfIndex_Object=MibTableColumn
arubaWiredDSSIfIndex=_ArubaWiredDSSIfIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,2),_ArubaWiredDSSIfIndex_Type())
arubaWiredDSSIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredDSSIfIndex.setStatus(_A)
class _ArubaWiredDSSIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_ArubaWiredDSSIfDescr_Type.__name__=_D
_ArubaWiredDSSIfDescr_Object=MibTableColumn
arubaWiredDSSIfDescr=_ArubaWiredDSSIfDescr_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,3),_ArubaWiredDSSIfDescr_Type())
arubaWiredDSSIfDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfDescr.setStatus(_A)
_ArubaWiredDSSIfInOctets_Type=Counter64
_ArubaWiredDSSIfInOctets_Object=MibTableColumn
arubaWiredDSSIfInOctets=_ArubaWiredDSSIfInOctets_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,4),_ArubaWiredDSSIfInOctets_Type())
arubaWiredDSSIfInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfInOctets.setStatus(_A)
_ArubaWiredDSSIfInUcastPkts_Type=Counter64
_ArubaWiredDSSIfInUcastPkts_Object=MibTableColumn
arubaWiredDSSIfInUcastPkts=_ArubaWiredDSSIfInUcastPkts_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,5),_ArubaWiredDSSIfInUcastPkts_Type())
arubaWiredDSSIfInUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfInUcastPkts.setStatus(_A)
_ArubaWiredDSSIfInDiscards_Type=Counter64
_ArubaWiredDSSIfInDiscards_Object=MibTableColumn
arubaWiredDSSIfInDiscards=_ArubaWiredDSSIfInDiscards_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,6),_ArubaWiredDSSIfInDiscards_Type())
arubaWiredDSSIfInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfInDiscards.setStatus(_A)
_ArubaWiredDSSIfInErrors_Type=Counter64
_ArubaWiredDSSIfInErrors_Object=MibTableColumn
arubaWiredDSSIfInErrors=_ArubaWiredDSSIfInErrors_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,7),_ArubaWiredDSSIfInErrors_Type())
arubaWiredDSSIfInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfInErrors.setStatus(_A)
_ArubaWiredDSSIfInUnknownProtos_Type=Counter64
_ArubaWiredDSSIfInUnknownProtos_Object=MibTableColumn
arubaWiredDSSIfInUnknownProtos=_ArubaWiredDSSIfInUnknownProtos_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,8),_ArubaWiredDSSIfInUnknownProtos_Type())
arubaWiredDSSIfInUnknownProtos.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfInUnknownProtos.setStatus(_A)
_ArubaWiredDSSIfInMulticastPkts_Type=Counter64
_ArubaWiredDSSIfInMulticastPkts_Object=MibTableColumn
arubaWiredDSSIfInMulticastPkts=_ArubaWiredDSSIfInMulticastPkts_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,9),_ArubaWiredDSSIfInMulticastPkts_Type())
arubaWiredDSSIfInMulticastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfInMulticastPkts.setStatus(_A)
_ArubaWiredDSSIfInBroadcastPkts_Type=Counter64
_ArubaWiredDSSIfInBroadcastPkts_Object=MibTableColumn
arubaWiredDSSIfInBroadcastPkts=_ArubaWiredDSSIfInBroadcastPkts_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,10),_ArubaWiredDSSIfInBroadcastPkts_Type())
arubaWiredDSSIfInBroadcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfInBroadcastPkts.setStatus(_A)
_ArubaWiredDSSIfOutOctets_Type=Counter64
_ArubaWiredDSSIfOutOctets_Object=MibTableColumn
arubaWiredDSSIfOutOctets=_ArubaWiredDSSIfOutOctets_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,11),_ArubaWiredDSSIfOutOctets_Type())
arubaWiredDSSIfOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfOutOctets.setStatus(_A)
_ArubaWiredDSSIfOutUcastPkts_Type=Counter64
_ArubaWiredDSSIfOutUcastPkts_Object=MibTableColumn
arubaWiredDSSIfOutUcastPkts=_ArubaWiredDSSIfOutUcastPkts_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,12),_ArubaWiredDSSIfOutUcastPkts_Type())
arubaWiredDSSIfOutUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfOutUcastPkts.setStatus(_A)
_ArubaWiredDSSIfOutDiscards_Type=Counter64
_ArubaWiredDSSIfOutDiscards_Object=MibTableColumn
arubaWiredDSSIfOutDiscards=_ArubaWiredDSSIfOutDiscards_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,13),_ArubaWiredDSSIfOutDiscards_Type())
arubaWiredDSSIfOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfOutDiscards.setStatus(_A)
_ArubaWiredDSSIfOutErrors_Type=Counter64
_ArubaWiredDSSIfOutErrors_Object=MibTableColumn
arubaWiredDSSIfOutErrors=_ArubaWiredDSSIfOutErrors_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,14),_ArubaWiredDSSIfOutErrors_Type())
arubaWiredDSSIfOutErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfOutErrors.setStatus(_A)
_ArubaWiredDSSIfOutMulticastPkts_Type=Counter64
_ArubaWiredDSSIfOutMulticastPkts_Object=MibTableColumn
arubaWiredDSSIfOutMulticastPkts=_ArubaWiredDSSIfOutMulticastPkts_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,15),_ArubaWiredDSSIfOutMulticastPkts_Type())
arubaWiredDSSIfOutMulticastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfOutMulticastPkts.setStatus(_A)
_ArubaWiredDSSIfOutBroadcastPkts_Type=Counter64
_ArubaWiredDSSIfOutBroadcastPkts_Object=MibTableColumn
arubaWiredDSSIfOutBroadcastPkts=_ArubaWiredDSSIfOutBroadcastPkts_Object((1,3,6,1,4,1,47196,4,1,1,3,25,2,1,1,16),_ArubaWiredDSSIfOutBroadcastPkts_Type())
arubaWiredDSSIfOutBroadcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDSSIfOutBroadcastPkts.setStatus(_A)
_ArubaWiredDSSConformance_ObjectIdentity=ObjectIdentity
arubaWiredDSSConformance=_ArubaWiredDSSConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,25,3))
_ArubaWiredDSSCompliances_ObjectIdentity=ObjectIdentity
arubaWiredDSSCompliances=_ArubaWiredDSSCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,25,3,1))
_ArubaWiredDSSGroups_ObjectIdentity=ObjectIdentity
arubaWiredDSSGroups=_ArubaWiredDSSGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,25,3,2))
arubaWiredDSMStatusTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,25,3,2,1))
arubaWiredDSMStatusTableGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:arubaWiredDSMStatusTableGroup.setStatus(_A)
arubaWiredDSSIfTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,25,3,2,2))
arubaWiredDSSIfTableGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:arubaWiredDSSIfTableGroup.setStatus(_A)
arubaWiredDSSMibCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,25,3,1,1))
arubaWiredDSSMibCompliance.setObjects(*((_B,_d),(_B,_e)))
if mibBuilder.loadTexts:arubaWiredDSSMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'arubaWiredDistServicesMIB':arubaWiredDistServicesMIB,'arubaWiredDSMStatus':arubaWiredDSMStatus,'arubaWiredDSMStatusTable':arubaWiredDSMStatusTable,'arubaWiredDSMStatusEntry':arubaWiredDSMStatusEntry,_G:arubaWiredDSMIndex,_J:arubaWiredDSMName,_K:arubaWiredDSMDescr,_L:arubaWiredDSMSerialNum,_M:arubaWiredDSMProductNum,_N:arubaWiredDSMPhysAddress,_O:arubaWiredDSMOperStatus,'arubaWiredDSSInterfaces':arubaWiredDSSInterfaces,'arubaWiredDSSIfTable':arubaWiredDSSIfTable,'arubaWiredDSSIfEntry':arubaWiredDSSIfEntry,_H:arubaWiredDSSModuleIndex,_I:arubaWiredDSSIfIndex,_P:arubaWiredDSSIfDescr,_Q:arubaWiredDSSIfInOctets,_R:arubaWiredDSSIfInUcastPkts,_S:arubaWiredDSSIfInDiscards,_T:arubaWiredDSSIfInErrors,_U:arubaWiredDSSIfInUnknownProtos,_V:arubaWiredDSSIfInMulticastPkts,_W:arubaWiredDSSIfInBroadcastPkts,_X:arubaWiredDSSIfOutOctets,_Y:arubaWiredDSSIfOutUcastPkts,_Z:arubaWiredDSSIfOutDiscards,_a:arubaWiredDSSIfOutErrors,_b:arubaWiredDSSIfOutMulticastPkts,_c:arubaWiredDSSIfOutBroadcastPkts,'arubaWiredDSSConformance':arubaWiredDSSConformance,'arubaWiredDSSCompliances':arubaWiredDSSCompliances,'arubaWiredDSSMibCompliance':arubaWiredDSSMibCompliance,'arubaWiredDSSGroups':arubaWiredDSSGroups,_d:arubaWiredDSMStatusTableGroup,_e:arubaWiredDSSIfTableGroup})