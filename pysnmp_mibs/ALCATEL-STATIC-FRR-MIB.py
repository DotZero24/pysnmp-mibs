_e='alcatelStaticFrrMplsInGroup'
_d='vRtrStaticFrrMplsXCOperStatus'
_c='vRtrStaticFrrMplsXCAdminStatus'
_b='vRtrStaticFrrMplsXCRowStatus'
_a='vRtrStaticFrrMplsXCOwner'
_Z='vRtrStaticFrrMplsXCIndexNext'
_Y='vRtrStaticFrrMplsOutSegmentRowStatus'
_X='vRtrStaticFrrMplsOutSegmentOwner'
_W='vRtrStaticFrrMplsOutSegmentXCIndex'
_V='vRtrStaticFrrMplsOutSegmentNextHopIpv4Addr'
_U='vRtrStaticFrrMplsOutSegmentNextHopIpAddrType'
_T='vRtrStaticFrrMplsOutSegmentTopLabel'
_S='vRtrStaticFrrMplsOutSegmentPushTopLabel'
_R='vRtrStaticFrrMplsOutSegmentIfIndex'
_Q='vRtrStaticFrrMplsOutSegmentIndexNext'
_P='vRtrStaticFrrMplsInSegmentRowStatus'
_O='vRtrStaticFrrMplsInSegmentOwner'
_N='vRtrStaticFrrMplsInSegmentXCIndex'
_M='vRtrStaticFrrMplsInSegmentNPop'
_L='InetAddressType'
_K='vRtrStaticFrrMplsXCIndex'
_J='MplsObjectOwner'
_I='vRtrStaticFrrMplsOutSegmentIndex'
_H='accessible-for-notify'
_G='vRtrStaticFrrMplsInSegmentLabel'
_F='vRtrStaticFrrMplsInSegmentIfIndex'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='ALCATEL-STATIC-FRR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1MplsFrr,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1MplsFrr')
TmnxOperState,=mibBuilder.importSymbols('ALCATEL-ENT1-TIMETRA-TC-MIB','TmnxOperState')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddressIPv4,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4',_L)
MplsLabel,MplsObjectOwner=mibBuilder.importSymbols('MPLS-LSR-MIB','MplsLabel',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
alcatelStaticFrrMIBModule=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,53,1))
if mibBuilder.loadTexts:alcatelStaticFrrMIBModule.setRevisions(('1909-02-02 00:00',))
_AlcatelStaticFrrMIBModuleObjs_ObjectIdentity=ObjectIdentity
alcatelStaticFrrMIBModuleObjs=_AlcatelStaticFrrMIBModuleObjs_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,53,1,1))
if mibBuilder.loadTexts:alcatelStaticFrrMIBModuleObjs.setStatus(_A)
_VRtrStaticFrrMplsInSegmentTable_Object=MibTable
vRtrStaticFrrMplsInSegmentTable=_VRtrStaticFrrMplsInSegmentTable_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,1))
if mibBuilder.loadTexts:vRtrStaticFrrMplsInSegmentTable.setStatus(_A)
_VRtrStaticFrrMplsInSegmentEntry_Object=MibTableRow
vRtrStaticFrrMplsInSegmentEntry=_VRtrStaticFrrMplsInSegmentEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,1,1))
vRtrStaticFrrMplsInSegmentEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:vRtrStaticFrrMplsInSegmentEntry.setStatus(_A)
_VRtrStaticFrrMplsInSegmentIfIndex_Type=InterfaceIndexOrZero
_VRtrStaticFrrMplsInSegmentIfIndex_Object=MibTableColumn
vRtrStaticFrrMplsInSegmentIfIndex=_VRtrStaticFrrMplsInSegmentIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,1,1,1),_VRtrStaticFrrMplsInSegmentIfIndex_Type())
vRtrStaticFrrMplsInSegmentIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:vRtrStaticFrrMplsInSegmentIfIndex.setStatus(_A)
_VRtrStaticFrrMplsInSegmentLabel_Type=MplsLabel
_VRtrStaticFrrMplsInSegmentLabel_Object=MibTableColumn
vRtrStaticFrrMplsInSegmentLabel=_VRtrStaticFrrMplsInSegmentLabel_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,1,1,2),_VRtrStaticFrrMplsInSegmentLabel_Type())
vRtrStaticFrrMplsInSegmentLabel.setMaxAccess(_H)
if mibBuilder.loadTexts:vRtrStaticFrrMplsInSegmentLabel.setStatus(_A)
class _VRtrStaticFrrMplsInSegmentNPop_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VRtrStaticFrrMplsInSegmentNPop_Type.__name__=_D
_VRtrStaticFrrMplsInSegmentNPop_Object=MibTableColumn
vRtrStaticFrrMplsInSegmentNPop=_VRtrStaticFrrMplsInSegmentNPop_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,1,1,3),_VRtrStaticFrrMplsInSegmentNPop_Type())
vRtrStaticFrrMplsInSegmentNPop.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsInSegmentNPop.setStatus(_A)
class _VRtrStaticFrrMplsInSegmentXCIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VRtrStaticFrrMplsInSegmentXCIndex_Type.__name__=_D
_VRtrStaticFrrMplsInSegmentXCIndex_Object=MibTableColumn
vRtrStaticFrrMplsInSegmentXCIndex=_VRtrStaticFrrMplsInSegmentXCIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,1,1,4),_VRtrStaticFrrMplsInSegmentXCIndex_Type())
vRtrStaticFrrMplsInSegmentXCIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrStaticFrrMplsInSegmentXCIndex.setStatus(_A)
class _VRtrStaticFrrMplsInSegmentOwner_Type(MplsObjectOwner):defaultValue=6
_VRtrStaticFrrMplsInSegmentOwner_Type.__name__=_J
_VRtrStaticFrrMplsInSegmentOwner_Object=MibTableColumn
vRtrStaticFrrMplsInSegmentOwner=_VRtrStaticFrrMplsInSegmentOwner_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,1,1,5),_VRtrStaticFrrMplsInSegmentOwner_Type())
vRtrStaticFrrMplsInSegmentOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsInSegmentOwner.setStatus(_A)
_VRtrStaticFrrMplsInSegmentRowStatus_Type=RowStatus
_VRtrStaticFrrMplsInSegmentRowStatus_Object=MibTableColumn
vRtrStaticFrrMplsInSegmentRowStatus=_VRtrStaticFrrMplsInSegmentRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,1,1,6),_VRtrStaticFrrMplsInSegmentRowStatus_Type())
vRtrStaticFrrMplsInSegmentRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsInSegmentRowStatus.setStatus(_A)
class _VRtrStaticFrrMplsOutSegmentIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VRtrStaticFrrMplsOutSegmentIndexNext_Type.__name__=_D
_VRtrStaticFrrMplsOutSegmentIndexNext_Object=MibScalar
vRtrStaticFrrMplsOutSegmentIndexNext=_VRtrStaticFrrMplsOutSegmentIndexNext_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,2),_VRtrStaticFrrMplsOutSegmentIndexNext_Type())
vRtrStaticFrrMplsOutSegmentIndexNext.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrStaticFrrMplsOutSegmentIndexNext.setStatus(_A)
_VRtrStaticFrrMplsOutSegmentTable_Object=MibTable
vRtrStaticFrrMplsOutSegmentTable=_VRtrStaticFrrMplsOutSegmentTable_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,3))
if mibBuilder.loadTexts:vRtrStaticFrrMplsOutSegmentTable.setStatus(_A)
_VRtrStaticFrrMplsOutSegmentEntry_Object=MibTableRow
vRtrStaticFrrMplsOutSegmentEntry=_VRtrStaticFrrMplsOutSegmentEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,3,1))
vRtrStaticFrrMplsOutSegmentEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:vRtrStaticFrrMplsOutSegmentEntry.setStatus(_A)
class _VRtrStaticFrrMplsOutSegmentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VRtrStaticFrrMplsOutSegmentIndex_Type.__name__=_D
_VRtrStaticFrrMplsOutSegmentIndex_Object=MibTableColumn
vRtrStaticFrrMplsOutSegmentIndex=_VRtrStaticFrrMplsOutSegmentIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,3,1,1),_VRtrStaticFrrMplsOutSegmentIndex_Type())
vRtrStaticFrrMplsOutSegmentIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:vRtrStaticFrrMplsOutSegmentIndex.setStatus(_A)
_VRtrStaticFrrMplsOutSegmentIfIndex_Type=InterfaceIndexOrZero
_VRtrStaticFrrMplsOutSegmentIfIndex_Object=MibTableColumn
vRtrStaticFrrMplsOutSegmentIfIndex=_VRtrStaticFrrMplsOutSegmentIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,3,1,2),_VRtrStaticFrrMplsOutSegmentIfIndex_Type())
vRtrStaticFrrMplsOutSegmentIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsOutSegmentIfIndex.setStatus(_A)
_VRtrStaticFrrMplsOutSegmentPushTopLabel_Type=TruthValue
_VRtrStaticFrrMplsOutSegmentPushTopLabel_Object=MibTableColumn
vRtrStaticFrrMplsOutSegmentPushTopLabel=_VRtrStaticFrrMplsOutSegmentPushTopLabel_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,3,1,3),_VRtrStaticFrrMplsOutSegmentPushTopLabel_Type())
vRtrStaticFrrMplsOutSegmentPushTopLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsOutSegmentPushTopLabel.setStatus(_A)
_VRtrStaticFrrMplsOutSegmentTopLabel_Type=MplsLabel
_VRtrStaticFrrMplsOutSegmentTopLabel_Object=MibTableColumn
vRtrStaticFrrMplsOutSegmentTopLabel=_VRtrStaticFrrMplsOutSegmentTopLabel_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,3,1,4),_VRtrStaticFrrMplsOutSegmentTopLabel_Type())
vRtrStaticFrrMplsOutSegmentTopLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsOutSegmentTopLabel.setStatus(_A)
class _VRtrStaticFrrMplsOutSegmentNextHopIpAddrType_Type(InetAddressType):defaultValue=0
_VRtrStaticFrrMplsOutSegmentNextHopIpAddrType_Type.__name__=_L
_VRtrStaticFrrMplsOutSegmentNextHopIpAddrType_Object=MibTableColumn
vRtrStaticFrrMplsOutSegmentNextHopIpAddrType=_VRtrStaticFrrMplsOutSegmentNextHopIpAddrType_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,3,1,5),_VRtrStaticFrrMplsOutSegmentNextHopIpAddrType_Type())
vRtrStaticFrrMplsOutSegmentNextHopIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsOutSegmentNextHopIpAddrType.setStatus(_A)
_VRtrStaticFrrMplsOutSegmentNextHopIpv4Addr_Type=IpAddress
_VRtrStaticFrrMplsOutSegmentNextHopIpv4Addr_Object=MibTableColumn
vRtrStaticFrrMplsOutSegmentNextHopIpv4Addr=_VRtrStaticFrrMplsOutSegmentNextHopIpv4Addr_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,3,1,6),_VRtrStaticFrrMplsOutSegmentNextHopIpv4Addr_Type())
vRtrStaticFrrMplsOutSegmentNextHopIpv4Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsOutSegmentNextHopIpv4Addr.setStatus(_A)
class _VRtrStaticFrrMplsOutSegmentXCIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VRtrStaticFrrMplsOutSegmentXCIndex_Type.__name__=_D
_VRtrStaticFrrMplsOutSegmentXCIndex_Object=MibTableColumn
vRtrStaticFrrMplsOutSegmentXCIndex=_VRtrStaticFrrMplsOutSegmentXCIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,3,1,7),_VRtrStaticFrrMplsOutSegmentXCIndex_Type())
vRtrStaticFrrMplsOutSegmentXCIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrStaticFrrMplsOutSegmentXCIndex.setStatus(_A)
class _VRtrStaticFrrMplsOutSegmentOwner_Type(MplsObjectOwner):defaultValue=6
_VRtrStaticFrrMplsOutSegmentOwner_Type.__name__=_J
_VRtrStaticFrrMplsOutSegmentOwner_Object=MibTableColumn
vRtrStaticFrrMplsOutSegmentOwner=_VRtrStaticFrrMplsOutSegmentOwner_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,3,1,8),_VRtrStaticFrrMplsOutSegmentOwner_Type())
vRtrStaticFrrMplsOutSegmentOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsOutSegmentOwner.setStatus(_A)
_VRtrStaticFrrMplsOutSegmentRowStatus_Type=RowStatus
_VRtrStaticFrrMplsOutSegmentRowStatus_Object=MibTableColumn
vRtrStaticFrrMplsOutSegmentRowStatus=_VRtrStaticFrrMplsOutSegmentRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,3,1,9),_VRtrStaticFrrMplsOutSegmentRowStatus_Type())
vRtrStaticFrrMplsOutSegmentRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsOutSegmentRowStatus.setStatus(_A)
class _VRtrStaticFrrMplsXCIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VRtrStaticFrrMplsXCIndexNext_Type.__name__=_D
_VRtrStaticFrrMplsXCIndexNext_Object=MibScalar
vRtrStaticFrrMplsXCIndexNext=_VRtrStaticFrrMplsXCIndexNext_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,4),_VRtrStaticFrrMplsXCIndexNext_Type())
vRtrStaticFrrMplsXCIndexNext.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrStaticFrrMplsXCIndexNext.setStatus(_A)
_VRtrStaticFrrMplsXCTable_Object=MibTable
vRtrStaticFrrMplsXCTable=_VRtrStaticFrrMplsXCTable_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,5))
if mibBuilder.loadTexts:vRtrStaticFrrMplsXCTable.setStatus(_A)
_VRtrStaticFrrMplsXCEntry_Object=MibTableRow
vRtrStaticFrrMplsXCEntry=_VRtrStaticFrrMplsXCEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,5,1))
vRtrStaticFrrMplsXCEntry.setIndexNames((0,_B,_K),(0,_B,_F),(0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:vRtrStaticFrrMplsXCEntry.setStatus(_A)
class _VRtrStaticFrrMplsXCIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VRtrStaticFrrMplsXCIndex_Type.__name__=_D
_VRtrStaticFrrMplsXCIndex_Object=MibTableColumn
vRtrStaticFrrMplsXCIndex=_VRtrStaticFrrMplsXCIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,5,1,1),_VRtrStaticFrrMplsXCIndex_Type())
vRtrStaticFrrMplsXCIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:vRtrStaticFrrMplsXCIndex.setStatus(_A)
_VRtrStaticFrrMplsXCOwner_Type=MplsObjectOwner
_VRtrStaticFrrMplsXCOwner_Object=MibTableColumn
vRtrStaticFrrMplsXCOwner=_VRtrStaticFrrMplsXCOwner_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,5,1,2),_VRtrStaticFrrMplsXCOwner_Type())
vRtrStaticFrrMplsXCOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsXCOwner.setStatus(_A)
_VRtrStaticFrrMplsXCRowStatus_Type=RowStatus
_VRtrStaticFrrMplsXCRowStatus_Object=MibTableColumn
vRtrStaticFrrMplsXCRowStatus=_VRtrStaticFrrMplsXCRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,5,1,3),_VRtrStaticFrrMplsXCRowStatus_Type())
vRtrStaticFrrMplsXCRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsXCRowStatus.setStatus(_A)
class _VRtrStaticFrrMplsXCAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_VRtrStaticFrrMplsXCAdminStatus_Type.__name__=_D
_VRtrStaticFrrMplsXCAdminStatus_Object=MibTableColumn
vRtrStaticFrrMplsXCAdminStatus=_VRtrStaticFrrMplsXCAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,5,1,4),_VRtrStaticFrrMplsXCAdminStatus_Type())
vRtrStaticFrrMplsXCAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrStaticFrrMplsXCAdminStatus.setStatus(_A)
class _VRtrStaticFrrMplsXCOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('up',1),('down',2),('unknown',4)))
_VRtrStaticFrrMplsXCOperStatus_Type.__name__=_D
_VRtrStaticFrrMplsXCOperStatus_Object=MibTableColumn
vRtrStaticFrrMplsXCOperStatus=_VRtrStaticFrrMplsXCOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,53,1,1,5,1,5),_VRtrStaticFrrMplsXCOperStatus_Type())
vRtrStaticFrrMplsXCOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrStaticFrrMplsXCOperStatus.setStatus(_A)
_AlcatelStaticFrrMIBConformance_ObjectIdentity=ObjectIdentity
alcatelStaticFrrMIBConformance=_AlcatelStaticFrrMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,53,1,2))
_AlcatelStaticFrrMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelStaticFrrMIBCompliances=_AlcatelStaticFrrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,53,1,2,1))
_AlcatelStaticFrrMIBGroups_ObjectIdentity=ObjectIdentity
alcatelStaticFrrMIBGroups=_AlcatelStaticFrrMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,53,1,2,2))
alcatelStaticFrrMplsInGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,53,1,2,2,1))
alcatelStaticFrrMplsInGroup.setObjects(*((_B,_F),(_B,_G),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:alcatelStaticFrrMplsInGroup.setStatus(_A)
alcatelStaticFrrMplsOutGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,53,1,2,2,2))
alcatelStaticFrrMplsOutGroup.setObjects(*((_B,_Q),(_B,_I),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:alcatelStaticFrrMplsOutGroup.setStatus(_A)
alcatelStaticFrrMplsXCGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,53,1,2,2,3))
alcatelStaticFrrMplsXCGroup.setObjects(*((_B,_Z),(_B,_K),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:alcatelStaticFrrMplsXCGroup.setStatus(_A)
alcatelStaticFrrCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,53,1,2,1,1))
alcatelStaticFrrCompliance.setObjects((_B,_e))
if mibBuilder.loadTexts:alcatelStaticFrrCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelStaticFrrMIBModule':alcatelStaticFrrMIBModule,'alcatelStaticFrrMIBModuleObjs':alcatelStaticFrrMIBModuleObjs,'vRtrStaticFrrMplsInSegmentTable':vRtrStaticFrrMplsInSegmentTable,'vRtrStaticFrrMplsInSegmentEntry':vRtrStaticFrrMplsInSegmentEntry,_F:vRtrStaticFrrMplsInSegmentIfIndex,_G:vRtrStaticFrrMplsInSegmentLabel,_M:vRtrStaticFrrMplsInSegmentNPop,_N:vRtrStaticFrrMplsInSegmentXCIndex,_O:vRtrStaticFrrMplsInSegmentOwner,_P:vRtrStaticFrrMplsInSegmentRowStatus,_Q:vRtrStaticFrrMplsOutSegmentIndexNext,'vRtrStaticFrrMplsOutSegmentTable':vRtrStaticFrrMplsOutSegmentTable,'vRtrStaticFrrMplsOutSegmentEntry':vRtrStaticFrrMplsOutSegmentEntry,_I:vRtrStaticFrrMplsOutSegmentIndex,_R:vRtrStaticFrrMplsOutSegmentIfIndex,_S:vRtrStaticFrrMplsOutSegmentPushTopLabel,_T:vRtrStaticFrrMplsOutSegmentTopLabel,_U:vRtrStaticFrrMplsOutSegmentNextHopIpAddrType,_V:vRtrStaticFrrMplsOutSegmentNextHopIpv4Addr,_W:vRtrStaticFrrMplsOutSegmentXCIndex,_X:vRtrStaticFrrMplsOutSegmentOwner,_Y:vRtrStaticFrrMplsOutSegmentRowStatus,_Z:vRtrStaticFrrMplsXCIndexNext,'vRtrStaticFrrMplsXCTable':vRtrStaticFrrMplsXCTable,'vRtrStaticFrrMplsXCEntry':vRtrStaticFrrMplsXCEntry,_K:vRtrStaticFrrMplsXCIndex,_a:vRtrStaticFrrMplsXCOwner,_b:vRtrStaticFrrMplsXCRowStatus,_c:vRtrStaticFrrMplsXCAdminStatus,_d:vRtrStaticFrrMplsXCOperStatus,'alcatelStaticFrrMIBConformance':alcatelStaticFrrMIBConformance,'alcatelStaticFrrMIBCompliances':alcatelStaticFrrMIBCompliances,'alcatelStaticFrrCompliance':alcatelStaticFrrCompliance,'alcatelStaticFrrMIBGroups':alcatelStaticFrrMIBGroups,_e:alcatelStaticFrrMplsInGroup,'alcatelStaticFrrMplsOutGroup':alcatelStaticFrrMplsOutGroup,'alcatelStaticFrrMplsXCGroup':alcatelStaticFrrMplsXCGroup})