_i='dlurConfGroup'
_h='dlurDlusSessnStatus'
_g='dlurPuDefBackupDlusName'
_f='dlurPuDefPrimDlusName'
_e='dlurPuActiveDlusName'
_d='dlurPuDlusSessnStatus'
_c='dlurPuLsName'
_b='dlurPuLocation'
_a='dlurPuAnsSupport'
_Z='dlurPuStatus'
_Y='dlurPuSscpSuppliedName'
_X='dlurDefaultDefBackupDlusName'
_W='dlurDefaultDefPrimDlusName'
_V='dlurNondisDlusDlurSessDeactSup'
_U='dlurNetworkNameForwardingSupport'
_T='dlurMultiSubnetSupport'
_S='dlurAnsSupport'
_R='dlurReleaseLevel'
_Q='dlurNodeCpName'
_P='dlurDlusName'
_O='dlurPuDefBackupDlusIndex'
_N='dlurPuDefBackupDlusPuName'
_M='pendingInactive'
_L='pendingActive'
_K='dlurPuName'
_J='dlurDefaultDefBackupDlusIndex'
_I='active'
_H='reset'
_G='Unsigned32'
_F='not-accessible'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='APPN-DLUR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnaControlPointName,=mibBuilder.importSymbols('APPN-MIB','SnaControlPointName')
snanauMIB,=mibBuilder.importSymbols('SNA-NAU-MIB','snanauMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
dlurMIB=ModuleIdentity((1,3,6,1,2,1,34,5))
_DlurObjects_ObjectIdentity=ObjectIdentity
dlurObjects=_DlurObjects_ObjectIdentity((1,3,6,1,2,1,34,5,1))
_DlurNodeInfo_ObjectIdentity=ObjectIdentity
dlurNodeInfo=_DlurNodeInfo_ObjectIdentity((1,3,6,1,2,1,34,5,1,1))
_DlurNodeCapabilities_ObjectIdentity=ObjectIdentity
dlurNodeCapabilities=_DlurNodeCapabilities_ObjectIdentity((1,3,6,1,2,1,34,5,1,1,1))
_DlurNodeCpName_Type=SnaControlPointName
_DlurNodeCpName_Object=MibScalar
dlurNodeCpName=_DlurNodeCpName_Object((1,3,6,1,2,1,34,5,1,1,1,1),_DlurNodeCpName_Type())
dlurNodeCpName.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurNodeCpName.setStatus(_A)
class _DlurReleaseLevel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_DlurReleaseLevel_Type.__name__=_D
_DlurReleaseLevel_Object=MibScalar
dlurReleaseLevel=_DlurReleaseLevel_Object((1,3,6,1,2,1,34,5,1,1,1,2),_DlurReleaseLevel_Type())
dlurReleaseLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurReleaseLevel.setStatus(_A)
class _DlurAnsSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('continueOrStop',1),('stopOnly',2)))
_DlurAnsSupport_Type.__name__=_E
_DlurAnsSupport_Object=MibScalar
dlurAnsSupport=_DlurAnsSupport_Object((1,3,6,1,2,1,34,5,1,1,1,3),_DlurAnsSupport_Type())
dlurAnsSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurAnsSupport.setStatus(_A)
_DlurMultiSubnetSupport_Type=TruthValue
_DlurMultiSubnetSupport_Object=MibScalar
dlurMultiSubnetSupport=_DlurMultiSubnetSupport_Object((1,3,6,1,2,1,34,5,1,1,1,4),_DlurMultiSubnetSupport_Type())
dlurMultiSubnetSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurMultiSubnetSupport.setStatus(_A)
_DlurDefaultDefPrimDlusName_Type=SnaControlPointName
_DlurDefaultDefPrimDlusName_Object=MibScalar
dlurDefaultDefPrimDlusName=_DlurDefaultDefPrimDlusName_Object((1,3,6,1,2,1,34,5,1,1,1,5),_DlurDefaultDefPrimDlusName_Type())
dlurDefaultDefPrimDlusName.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurDefaultDefPrimDlusName.setStatus(_A)
_DlurNetworkNameForwardingSupport_Type=TruthValue
_DlurNetworkNameForwardingSupport_Object=MibScalar
dlurNetworkNameForwardingSupport=_DlurNetworkNameForwardingSupport_Object((1,3,6,1,2,1,34,5,1,1,1,6),_DlurNetworkNameForwardingSupport_Type())
dlurNetworkNameForwardingSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurNetworkNameForwardingSupport.setStatus(_A)
_DlurNondisDlusDlurSessDeactSup_Type=TruthValue
_DlurNondisDlusDlurSessDeactSup_Object=MibScalar
dlurNondisDlusDlurSessDeactSup=_DlurNondisDlusDlurSessDeactSup_Object((1,3,6,1,2,1,34,5,1,1,1,7),_DlurNondisDlusDlurSessDeactSup_Type())
dlurNondisDlusDlurSessDeactSup.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurNondisDlusDlurSessDeactSup.setStatus(_A)
_DlurDefaultDefBackupDlusTable_Object=MibTable
dlurDefaultDefBackupDlusTable=_DlurDefaultDefBackupDlusTable_Object((1,3,6,1,2,1,34,5,1,1,2))
if mibBuilder.loadTexts:dlurDefaultDefBackupDlusTable.setStatus(_A)
_DlurDefaultDefBackupDlusEntry_Object=MibTableRow
dlurDefaultDefBackupDlusEntry=_DlurDefaultDefBackupDlusEntry_Object((1,3,6,1,2,1,34,5,1,1,2,1))
dlurDefaultDefBackupDlusEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:dlurDefaultDefBackupDlusEntry.setStatus(_A)
class _DlurDefaultDefBackupDlusIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_DlurDefaultDefBackupDlusIndex_Type.__name__=_G
_DlurDefaultDefBackupDlusIndex_Object=MibTableColumn
dlurDefaultDefBackupDlusIndex=_DlurDefaultDefBackupDlusIndex_Object((1,3,6,1,2,1,34,5,1,1,2,1,1),_DlurDefaultDefBackupDlusIndex_Type())
dlurDefaultDefBackupDlusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:dlurDefaultDefBackupDlusIndex.setStatus(_A)
_DlurDefaultDefBackupDlusName_Type=SnaControlPointName
_DlurDefaultDefBackupDlusName_Object=MibTableColumn
dlurDefaultDefBackupDlusName=_DlurDefaultDefBackupDlusName_Object((1,3,6,1,2,1,34,5,1,1,2,1,2),_DlurDefaultDefBackupDlusName_Type())
dlurDefaultDefBackupDlusName.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurDefaultDefBackupDlusName.setStatus(_A)
_DlurPuInfo_ObjectIdentity=ObjectIdentity
dlurPuInfo=_DlurPuInfo_ObjectIdentity((1,3,6,1,2,1,34,5,1,2))
_DlurPuTable_Object=MibTable
dlurPuTable=_DlurPuTable_Object((1,3,6,1,2,1,34,5,1,2,1))
if mibBuilder.loadTexts:dlurPuTable.setStatus(_A)
_DlurPuEntry_Object=MibTableRow
dlurPuEntry=_DlurPuEntry_Object((1,3,6,1,2,1,34,5,1,2,1,1))
dlurPuEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:dlurPuEntry.setStatus(_A)
class _DlurPuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,17))
_DlurPuName_Type.__name__=_D
_DlurPuName_Object=MibTableColumn
dlurPuName=_DlurPuName_Object((1,3,6,1,2,1,34,5,1,2,1,1,1),_DlurPuName_Type())
dlurPuName.setMaxAccess(_F)
if mibBuilder.loadTexts:dlurPuName.setStatus(_A)
class _DlurPuSscpSuppliedName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_DlurPuSscpSuppliedName_Type.__name__=_D
_DlurPuSscpSuppliedName_Object=MibTableColumn
dlurPuSscpSuppliedName=_DlurPuSscpSuppliedName_Object((1,3,6,1,2,1,34,5,1,2,1,1,2),_DlurPuSscpSuppliedName_Type())
dlurPuSscpSuppliedName.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurPuSscpSuppliedName.setStatus(_A)
class _DlurPuStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_H,1),('pendReqActpuRsp',2),('pendActpu',3),('pendActpuRsp',4),(_I,5),('pendLinkact',6),('pendDactpuRsp',7),('pendInop',8),('pendInopActpu',9)))
_DlurPuStatus_Type.__name__=_E
_DlurPuStatus_Object=MibTableColumn
dlurPuStatus=_DlurPuStatus_Object((1,3,6,1,2,1,34,5,1,2,1,1,3),_DlurPuStatus_Type())
dlurPuStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurPuStatus.setStatus(_A)
class _DlurPuAnsSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('continue',1),('stop',2)))
_DlurPuAnsSupport_Type.__name__=_E
_DlurPuAnsSupport_Object=MibTableColumn
dlurPuAnsSupport=_DlurPuAnsSupport_Object((1,3,6,1,2,1,34,5,1,2,1,1,4),_DlurPuAnsSupport_Type())
dlurPuAnsSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurPuAnsSupport.setStatus(_A)
class _DlurPuLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('downstream',2)))
_DlurPuLocation_Type.__name__=_E
_DlurPuLocation_Object=MibTableColumn
dlurPuLocation=_DlurPuLocation_Object((1,3,6,1,2,1,34,5,1,2,1,1,5),_DlurPuLocation_Type())
dlurPuLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurPuLocation.setStatus(_A)
class _DlurPuLsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_DlurPuLsName_Type.__name__=_D
_DlurPuLsName_Object=MibTableColumn
dlurPuLsName=_DlurPuLsName_Object((1,3,6,1,2,1,34,5,1,2,1,1,6),_DlurPuLsName_Type())
dlurPuLsName.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurPuLsName.setStatus(_A)
class _DlurPuDlusSessnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_L,2),(_I,3),(_M,4)))
_DlurPuDlusSessnStatus_Type.__name__=_E
_DlurPuDlusSessnStatus_Object=MibTableColumn
dlurPuDlusSessnStatus=_DlurPuDlusSessnStatus_Object((1,3,6,1,2,1,34,5,1,2,1,1,7),_DlurPuDlusSessnStatus_Type())
dlurPuDlusSessnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurPuDlusSessnStatus.setStatus(_A)
class _DlurPuActiveDlusName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_DlurPuActiveDlusName_Type.__name__=_D
_DlurPuActiveDlusName_Object=MibTableColumn
dlurPuActiveDlusName=_DlurPuActiveDlusName_Object((1,3,6,1,2,1,34,5,1,2,1,1,8),_DlurPuActiveDlusName_Type())
dlurPuActiveDlusName.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurPuActiveDlusName.setStatus(_A)
class _DlurPuDefPrimDlusName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_DlurPuDefPrimDlusName_Type.__name__=_D
_DlurPuDefPrimDlusName_Object=MibTableColumn
dlurPuDefPrimDlusName=_DlurPuDefPrimDlusName_Object((1,3,6,1,2,1,34,5,1,2,1,1,9),_DlurPuDefPrimDlusName_Type())
dlurPuDefPrimDlusName.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurPuDefPrimDlusName.setStatus(_A)
_DlurPuDefBackupDlusTable_Object=MibTable
dlurPuDefBackupDlusTable=_DlurPuDefBackupDlusTable_Object((1,3,6,1,2,1,34,5,1,2,2))
if mibBuilder.loadTexts:dlurPuDefBackupDlusTable.setStatus(_A)
_DlurPuDefBackupDlusEntry_Object=MibTableRow
dlurPuDefBackupDlusEntry=_DlurPuDefBackupDlusEntry_Object((1,3,6,1,2,1,34,5,1,2,2,1))
dlurPuDefBackupDlusEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:dlurPuDefBackupDlusEntry.setStatus(_A)
class _DlurPuDefBackupDlusPuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,17))
_DlurPuDefBackupDlusPuName_Type.__name__=_D
_DlurPuDefBackupDlusPuName_Object=MibTableColumn
dlurPuDefBackupDlusPuName=_DlurPuDefBackupDlusPuName_Object((1,3,6,1,2,1,34,5,1,2,2,1,1),_DlurPuDefBackupDlusPuName_Type())
dlurPuDefBackupDlusPuName.setMaxAccess(_F)
if mibBuilder.loadTexts:dlurPuDefBackupDlusPuName.setStatus(_A)
class _DlurPuDefBackupDlusIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_DlurPuDefBackupDlusIndex_Type.__name__=_G
_DlurPuDefBackupDlusIndex_Object=MibTableColumn
dlurPuDefBackupDlusIndex=_DlurPuDefBackupDlusIndex_Object((1,3,6,1,2,1,34,5,1,2,2,1,2),_DlurPuDefBackupDlusIndex_Type())
dlurPuDefBackupDlusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:dlurPuDefBackupDlusIndex.setStatus(_A)
_DlurPuDefBackupDlusName_Type=SnaControlPointName
_DlurPuDefBackupDlusName_Object=MibTableColumn
dlurPuDefBackupDlusName=_DlurPuDefBackupDlusName_Object((1,3,6,1,2,1,34,5,1,2,2,1,3),_DlurPuDefBackupDlusName_Type())
dlurPuDefBackupDlusName.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurPuDefBackupDlusName.setStatus(_A)
_DlurDlusInfo_ObjectIdentity=ObjectIdentity
dlurDlusInfo=_DlurDlusInfo_ObjectIdentity((1,3,6,1,2,1,34,5,1,3))
_DlurDlusTable_Object=MibTable
dlurDlusTable=_DlurDlusTable_Object((1,3,6,1,2,1,34,5,1,3,1))
if mibBuilder.loadTexts:dlurDlusTable.setStatus(_A)
_DlurDlusEntry_Object=MibTableRow
dlurDlusEntry=_DlurDlusEntry_Object((1,3,6,1,2,1,34,5,1,3,1,1))
dlurDlusEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:dlurDlusEntry.setStatus(_A)
_DlurDlusName_Type=SnaControlPointName
_DlurDlusName_Object=MibTableColumn
dlurDlusName=_DlurDlusName_Object((1,3,6,1,2,1,34,5,1,3,1,1,1),_DlurDlusName_Type())
dlurDlusName.setMaxAccess(_F)
if mibBuilder.loadTexts:dlurDlusName.setStatus(_A)
class _DlurDlusSessnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_L,2),(_I,3),(_M,4)))
_DlurDlusSessnStatus_Type.__name__=_E
_DlurDlusSessnStatus_Object=MibTableColumn
dlurDlusSessnStatus=_DlurDlusSessnStatus_Object((1,3,6,1,2,1,34,5,1,3,1,1,2),_DlurDlusSessnStatus_Type())
dlurDlusSessnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlurDlusSessnStatus.setStatus(_A)
_DlurConformance_ObjectIdentity=ObjectIdentity
dlurConformance=_DlurConformance_ObjectIdentity((1,3,6,1,2,1,34,5,2))
_DlurCompliances_ObjectIdentity=ObjectIdentity
dlurCompliances=_DlurCompliances_ObjectIdentity((1,3,6,1,2,1,34,5,2,1))
_DlurGroups_ObjectIdentity=ObjectIdentity
dlurGroups=_DlurGroups_ObjectIdentity((1,3,6,1,2,1,34,5,2,2))
dlurConfGroup=ObjectGroup((1,3,6,1,2,1,34,5,2,2,1))
dlurConfGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:dlurConfGroup.setStatus(_A)
dlurCompliance=ModuleCompliance((1,3,6,1,2,1,34,5,2,1,1))
dlurCompliance.setObjects((_B,_i))
if mibBuilder.loadTexts:dlurCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlurMIB':dlurMIB,'dlurObjects':dlurObjects,'dlurNodeInfo':dlurNodeInfo,'dlurNodeCapabilities':dlurNodeCapabilities,_Q:dlurNodeCpName,_R:dlurReleaseLevel,_S:dlurAnsSupport,_T:dlurMultiSubnetSupport,_W:dlurDefaultDefPrimDlusName,_U:dlurNetworkNameForwardingSupport,_V:dlurNondisDlusDlurSessDeactSup,'dlurDefaultDefBackupDlusTable':dlurDefaultDefBackupDlusTable,'dlurDefaultDefBackupDlusEntry':dlurDefaultDefBackupDlusEntry,_J:dlurDefaultDefBackupDlusIndex,_X:dlurDefaultDefBackupDlusName,'dlurPuInfo':dlurPuInfo,'dlurPuTable':dlurPuTable,'dlurPuEntry':dlurPuEntry,_K:dlurPuName,_Y:dlurPuSscpSuppliedName,_Z:dlurPuStatus,_a:dlurPuAnsSupport,_b:dlurPuLocation,_c:dlurPuLsName,_d:dlurPuDlusSessnStatus,_e:dlurPuActiveDlusName,_f:dlurPuDefPrimDlusName,'dlurPuDefBackupDlusTable':dlurPuDefBackupDlusTable,'dlurPuDefBackupDlusEntry':dlurPuDefBackupDlusEntry,_N:dlurPuDefBackupDlusPuName,_O:dlurPuDefBackupDlusIndex,_g:dlurPuDefBackupDlusName,'dlurDlusInfo':dlurDlusInfo,'dlurDlusTable':dlurDlusTable,'dlurDlusEntry':dlurDlusEntry,_P:dlurDlusName,_h:dlurDlusSessnStatus,'dlurConformance':dlurConformance,'dlurCompliances':dlurCompliances,'dlurCompliance':dlurCompliance,'dlurGroups':dlurGroups,_i:dlurConfGroup})