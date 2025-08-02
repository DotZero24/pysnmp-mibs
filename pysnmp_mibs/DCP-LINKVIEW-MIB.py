_W='dcpLinkviewTableGroupV1'
_V='dcpLinkviewRemoteHostname'
_U='dcpLinkviewRemoteName'
_T='dcpLinkviewRemotePower'
_S='dcpLinkviewFiberUtilization'
_R='dcpLinkviewFiberDispFinal'
_Q='dcpLinkviewFiberDispComp'
_P='dcpLinkviewFiberType'
_O='dcpLinkviewFiberDispersion'
_N='dcpLinkviewFiberLength'
_M='dcpLinkviewFiberAttenuation'
_L='dcpLinkviewFiberLoss'
_K='dcpLinkviewLocalPower'
_J='dcpLinkviewLocalStatus'
_I='dcpLinkviewLocalName'
_H='dcpLinkviewLocalHostname'
_G='dcpLinkviewIndex'
_F='Gauge32'
_E='Unsigned32'
_D='Integer32'
_C='read-only'
_B='DCP-LINKVIEW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dcpGeneric,=mibBuilder.importSymbols('DCP-MIB','dcpGeneric')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_F,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
InterfaceStatus,OpticalPower1Decimal=mibBuilder.importSymbols('SO-TC-MIB','InterfaceStatus','OpticalPower1Decimal')
dcpLinkview=ModuleIdentity((1,3,6,1,4,1,30826,2,2,3))
if mibBuilder.loadTexts:dcpLinkview.setRevisions(('2021-02-25 12:00','2018-10-08 14:44'))
class DcpFiberLoss(TextualConvention,Unsigned32):status=_A;displayHint='d-1';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
class DcpFiberAttenuation(TextualConvention,Unsigned32):status=_A;displayHint='d-2';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
class DcpFiberLength(TextualConvention,Unsigned32):status=_A;displayHint='d-1';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_DcpLinkviewObjects_ObjectIdentity=ObjectIdentity
dcpLinkviewObjects=_DcpLinkviewObjects_ObjectIdentity((1,3,6,1,4,1,30826,2,2,3,1))
_DcpLinkviewTable_Object=MibTable
dcpLinkviewTable=_DcpLinkviewTable_Object((1,3,6,1,4,1,30826,2,2,3,1,1))
if mibBuilder.loadTexts:dcpLinkviewTable.setStatus(_A)
_DcpLinkviewEntry_Object=MibTableRow
dcpLinkviewEntry=_DcpLinkviewEntry_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1))
dcpLinkviewEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:dcpLinkviewEntry.setStatus(_A)
class _DcpLinkviewIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_DcpLinkviewIndex_Type.__name__=_E
_DcpLinkviewIndex_Object=MibTableColumn
dcpLinkviewIndex=_DcpLinkviewIndex_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,1),_DcpLinkviewIndex_Type())
dcpLinkviewIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dcpLinkviewIndex.setStatus(_A)
_DcpLinkviewLocalHostname_Type=DisplayString
_DcpLinkviewLocalHostname_Object=MibTableColumn
dcpLinkviewLocalHostname=_DcpLinkviewLocalHostname_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,2),_DcpLinkviewLocalHostname_Type())
dcpLinkviewLocalHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewLocalHostname.setStatus(_A)
_DcpLinkviewLocalName_Type=DisplayString
_DcpLinkviewLocalName_Object=MibTableColumn
dcpLinkviewLocalName=_DcpLinkviewLocalName_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,3),_DcpLinkviewLocalName_Type())
dcpLinkviewLocalName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewLocalName.setStatus(_A)
_DcpLinkviewLocalStatus_Type=InterfaceStatus
_DcpLinkviewLocalStatus_Object=MibTableColumn
dcpLinkviewLocalStatus=_DcpLinkviewLocalStatus_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,4),_DcpLinkviewLocalStatus_Type())
dcpLinkviewLocalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewLocalStatus.setStatus(_A)
_DcpLinkviewLocalPower_Type=OpticalPower1Decimal
_DcpLinkviewLocalPower_Object=MibTableColumn
dcpLinkviewLocalPower=_DcpLinkviewLocalPower_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,5),_DcpLinkviewLocalPower_Type())
dcpLinkviewLocalPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewLocalPower.setStatus(_A)
_DcpLinkviewFiberLoss_Type=DcpFiberLoss
_DcpLinkviewFiberLoss_Object=MibTableColumn
dcpLinkviewFiberLoss=_DcpLinkviewFiberLoss_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,6),_DcpLinkviewFiberLoss_Type())
dcpLinkviewFiberLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewFiberLoss.setStatus(_A)
_DcpLinkviewFiberAttenuation_Type=DcpFiberAttenuation
_DcpLinkviewFiberAttenuation_Object=MibTableColumn
dcpLinkviewFiberAttenuation=_DcpLinkviewFiberAttenuation_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,7),_DcpLinkviewFiberAttenuation_Type())
dcpLinkviewFiberAttenuation.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewFiberAttenuation.setStatus(_A)
_DcpLinkviewFiberLength_Type=DcpFiberLength
_DcpLinkviewFiberLength_Object=MibTableColumn
dcpLinkviewFiberLength=_DcpLinkviewFiberLength_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,8),_DcpLinkviewFiberLength_Type())
dcpLinkviewFiberLength.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewFiberLength.setStatus(_A)
class _DcpLinkviewFiberDispersion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_DcpLinkviewFiberDispersion_Type.__name__=_E
_DcpLinkviewFiberDispersion_Object=MibTableColumn
dcpLinkviewFiberDispersion=_DcpLinkviewFiberDispersion_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,9),_DcpLinkviewFiberDispersion_Type())
dcpLinkviewFiberDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewFiberDispersion.setStatus(_A)
_DcpLinkviewFiberType_Type=DisplayString
_DcpLinkviewFiberType_Object=MibTableColumn
dcpLinkviewFiberType=_DcpLinkviewFiberType_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,10),_DcpLinkviewFiberType_Type())
dcpLinkviewFiberType.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewFiberType.setStatus(_A)
class _DcpLinkviewFiberDispComp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10000,10000))
_DcpLinkviewFiberDispComp_Type.__name__=_D
_DcpLinkviewFiberDispComp_Object=MibTableColumn
dcpLinkviewFiberDispComp=_DcpLinkviewFiberDispComp_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,11),_DcpLinkviewFiberDispComp_Type())
dcpLinkviewFiberDispComp.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewFiberDispComp.setStatus(_A)
class _DcpLinkviewFiberDispFinal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10000,10000))
_DcpLinkviewFiberDispFinal_Type.__name__=_D
_DcpLinkviewFiberDispFinal_Object=MibTableColumn
dcpLinkviewFiberDispFinal=_DcpLinkviewFiberDispFinal_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,12),_DcpLinkviewFiberDispFinal_Type())
dcpLinkviewFiberDispFinal.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewFiberDispFinal.setStatus(_A)
class _DcpLinkviewFiberUtilization_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DcpLinkviewFiberUtilization_Type.__name__=_F
_DcpLinkviewFiberUtilization_Object=MibTableColumn
dcpLinkviewFiberUtilization=_DcpLinkviewFiberUtilization_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,13),_DcpLinkviewFiberUtilization_Type())
dcpLinkviewFiberUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewFiberUtilization.setStatus(_A)
_DcpLinkviewRemotePower_Type=OpticalPower1Decimal
_DcpLinkviewRemotePower_Object=MibTableColumn
dcpLinkviewRemotePower=_DcpLinkviewRemotePower_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,14),_DcpLinkviewRemotePower_Type())
dcpLinkviewRemotePower.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewRemotePower.setStatus(_A)
_DcpLinkviewRemoteName_Type=DisplayString
_DcpLinkviewRemoteName_Object=MibTableColumn
dcpLinkviewRemoteName=_DcpLinkviewRemoteName_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,15),_DcpLinkviewRemoteName_Type())
dcpLinkviewRemoteName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewRemoteName.setStatus(_A)
_DcpLinkviewRemoteHostname_Type=DisplayString
_DcpLinkviewRemoteHostname_Object=MibTableColumn
dcpLinkviewRemoteHostname=_DcpLinkviewRemoteHostname_Object((1,3,6,1,4,1,30826,2,2,3,1,1,1,16),_DcpLinkviewRemoteHostname_Type())
dcpLinkviewRemoteHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpLinkviewRemoteHostname.setStatus(_A)
_DcpLinkviewMIBCompliance_ObjectIdentity=ObjectIdentity
dcpLinkviewMIBCompliance=_DcpLinkviewMIBCompliance_ObjectIdentity((1,3,6,1,4,1,30826,2,2,3,2))
_DcpLinkviewMIBGroups_ObjectIdentity=ObjectIdentity
dcpLinkviewMIBGroups=_DcpLinkviewMIBGroups_ObjectIdentity((1,3,6,1,4,1,30826,2,2,3,2,1))
_DcpLinkviewMIBCompliances_ObjectIdentity=ObjectIdentity
dcpLinkviewMIBCompliances=_DcpLinkviewMIBCompliances_ObjectIdentity((1,3,6,1,4,1,30826,2,2,3,2,2))
dcpLinkviewTableGroupV1=ObjectGroup((1,3,6,1,4,1,30826,2,2,3,2,1,1))
dcpLinkviewTableGroupV1.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:dcpLinkviewTableGroupV1.setStatus(_A)
dcpLinkviewBasicComplV1=ModuleCompliance((1,3,6,1,4,1,30826,2,2,3,2,2,1))
dcpLinkviewBasicComplV1.setObjects((_B,_W))
if mibBuilder.loadTexts:dcpLinkviewBasicComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DcpFiberLoss':DcpFiberLoss,'DcpFiberAttenuation':DcpFiberAttenuation,'DcpFiberLength':DcpFiberLength,'dcpLinkview':dcpLinkview,'dcpLinkviewObjects':dcpLinkviewObjects,'dcpLinkviewTable':dcpLinkviewTable,'dcpLinkviewEntry':dcpLinkviewEntry,_G:dcpLinkviewIndex,_H:dcpLinkviewLocalHostname,_I:dcpLinkviewLocalName,_J:dcpLinkviewLocalStatus,_K:dcpLinkviewLocalPower,_L:dcpLinkviewFiberLoss,_M:dcpLinkviewFiberAttenuation,_N:dcpLinkviewFiberLength,_O:dcpLinkviewFiberDispersion,_P:dcpLinkviewFiberType,_Q:dcpLinkviewFiberDispComp,_R:dcpLinkviewFiberDispFinal,_S:dcpLinkviewFiberUtilization,_T:dcpLinkviewRemotePower,_U:dcpLinkviewRemoteName,_V:dcpLinkviewRemoteHostname,'dcpLinkviewMIBCompliance':dcpLinkviewMIBCompliance,'dcpLinkviewMIBGroups':dcpLinkviewMIBGroups,_W:dcpLinkviewTableGroupV1,'dcpLinkviewMIBCompliances':dcpLinkviewMIBCompliances,'dcpLinkviewBasicComplV1':dcpLinkviewBasicComplV1})