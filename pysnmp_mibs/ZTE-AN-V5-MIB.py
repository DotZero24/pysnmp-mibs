_n='zxAnV5UaLinkDsx1TsNo'
_m='zxAnV5UaLinkDsx1LinkNo'
_l='zxAnV5UaLinkSlot'
_k='zxAnV5UaLinkShelf'
_j='zxAnV5UaLinkRack'
_i='v5LinkTsNo'
_h='v5LinkTsLinkID'
_g='v5LinkTsV5IID'
_f='isdnEfAddr'
_e='isdnV5IID'
_d='ctrlBusy'
_c='ctrlIdle'
_b='v5UpBusy'
_a='vtUpIdle'
_Z='v5UpStop'
_Y='active'
_X='pstnL3Addr'
_W='pstnV5IID'
_V='v5LchLcci'
_U='v5LchV5IID'
_T='v5PchLinkTs'
_S='v5PchLinkId'
_R='v5PchV5IID'
_Q='tsUsed'
_P='v5LinkID'
_O='v5LinkV5IID'
_N='v5IFID'
_M='Unsigned32'
_L='read-write'
_K='tsUnUsed'
_J='flagCreated'
_I='flagNotCreated'
_H='dlAbNormal'
_G='dlNormal'
_F='not-accessible'
_E='ZTE-AN-V5-MIB'
_D='read-only'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAnV5Mib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5200))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_MsagmajorVersion_ObjectIdentity=ObjectIdentity
msagmajorVersion=_MsagmajorVersion_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3))
_MsagV5Service_ObjectIdentity=ObjectIdentity
msagV5Service=_MsagV5Service_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,5))
_V5InterfaceTable_Object=MibTable
v5InterfaceTable=_V5InterfaceTable_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1))
if mibBuilder.loadTexts:v5InterfaceTable.setStatus(_A)
_V5InterfaceEntry_Object=MibTableRow
v5InterfaceEntry=_V5InterfaceEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1))
v5InterfaceEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:v5InterfaceEntry.setStatus(_A)
_V5IFID_Type=Unsigned32
_V5IFID_Object=MibTableColumn
v5IFID=_V5IFID_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,1),_V5IFID_Type())
v5IFID.setMaxAccess(_F)
if mibBuilder.loadTexts:v5IFID.setStatus(_A)
class _V5IFType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('v51Type',1),('v52Type',2)))
_V5IFType_Type.__name__=_B
_V5IFType_Object=MibTableColumn
v5IFType=_V5IFType_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,2),_V5IFType_Type())
v5IFType.setMaxAccess(_C)
if mibBuilder.loadTexts:v5IFType.setStatus(_A)
class _V5IFVar_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_V5IFVar_Type.__name__=_B
_V5IFVar_Object=MibTableColumn
v5IFVar=_V5IFVar_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,3),_V5IFVar_Type())
v5IFVar.setMaxAccess(_C)
if mibBuilder.loadTexts:v5IFVar.setStatus(_A)
class _V5IFLeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('leNormal',0),('leF_150',1),('leS11240',2),('leL_5ESS',3),('leC_C08',4),('leEWSD',5),('leDMS',6),('leSP30',7),('leNec',8),('leHJD04',9),('leSTND',10),('leCompliance',11)))
_V5IFLeType_Type.__name__=_B
_V5IFLeType_Object=MibTableColumn
v5IFLeType=_V5IFLeType_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,4),_V5IFLeType_Type())
v5IFLeType.setMaxAccess(_C)
if mibBuilder.loadTexts:v5IFLeType.setStatus(_A)
class _V5IFStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,255)));namedValues=NamedValues(*(('inDeactive',0),('inActive',1),('inCtrlDeactive',2),('inInvalid',255)))
_V5IFStatus_Type.__name__=_B
_V5IFStatus_Object=MibTableColumn
v5IFStatus=_V5IFStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,5),_V5IFStatus_Type())
v5IFStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:v5IFStatus.setStatus(_A)
class _V5IFCommCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('commNormal',0),('commStop',1)))
_V5IFCommCtrlStatus_Type.__name__=_B
_V5IFCommCtrlStatus_Object=MibTableColumn
v5IFCommCtrlStatus=_V5IFCommCtrlStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,6),_V5IFCommCtrlStatus_Type())
v5IFCommCtrlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:v5IFCommCtrlStatus.setStatus(_A)
class _V5IFPstnDLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_V5IFPstnDLStatus_Type.__name__=_B
_V5IFPstnDLStatus_Object=MibTableColumn
v5IFPstnDLStatus=_V5IFPstnDLStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,7),_V5IFPstnDLStatus_Type())
v5IFPstnDLStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:v5IFPstnDLStatus.setStatus(_A)
class _V5IFBccDLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_V5IFBccDLStatus_Type.__name__=_B
_V5IFBccDLStatus_Object=MibTableColumn
v5IFBccDLStatus=_V5IFBccDLStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,8),_V5IFBccDLStatus_Type())
v5IFBccDLStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:v5IFBccDLStatus.setStatus(_A)
class _V5IFLinkDLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_V5IFLinkDLStatus_Type.__name__=_B
_V5IFLinkDLStatus_Object=MibTableColumn
v5IFLinkDLStatus=_V5IFLinkDLStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,9),_V5IFLinkDLStatus_Type())
v5IFLinkDLStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:v5IFLinkDLStatus.setStatus(_A)
class _V5IFCtrlDLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_V5IFCtrlDLStatus_Type.__name__=_B
_V5IFCtrlDLStatus_Object=MibTableColumn
v5IFCtrlDLStatus=_V5IFCtrlDLStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,10),_V5IFCtrlDLStatus_Type())
v5IFCtrlDLStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:v5IFCtrlDLStatus.setStatus(_A)
class _V5IFProtMDLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_V5IFProtMDLStatus_Type.__name__=_B
_V5IFProtMDLStatus_Object=MibTableColumn
v5IFProtMDLStatus=_V5IFProtMDLStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,11),_V5IFProtMDLStatus_Type())
v5IFProtMDLStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:v5IFProtMDLStatus.setStatus(_A)
class _V5IFProtBDLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_V5IFProtBDLStatus_Type.__name__=_B
_V5IFProtBDLStatus_Object=MibTableColumn
v5IFProtBDLStatus=_V5IFProtBDLStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,12),_V5IFProtBDLStatus_Type())
v5IFProtBDLStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:v5IFProtBDLStatus.setStatus(_A)
_V5IFNewV5IID_Type=Unsigned32
_V5IFNewV5IID_Object=MibTableColumn
v5IFNewV5IID=_V5IFNewV5IID_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,13),_V5IFNewV5IID_Type())
v5IFNewV5IID.setMaxAccess(_C)
if mibBuilder.loadTexts:v5IFNewV5IID.setStatus(_A)
_V5IFRowStatus_Type=RowStatus
_V5IFRowStatus_Object=MibTableColumn
v5IFRowStatus=_V5IFRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,1,1,14),_V5IFRowStatus_Type())
v5IFRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:v5IFRowStatus.setStatus(_A)
_V5LinkTable_Object=MibTable
v5LinkTable=_V5LinkTable_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3))
if mibBuilder.loadTexts:v5LinkTable.setStatus(_A)
_V5LinkEntry_Object=MibTableRow
v5LinkEntry=_V5LinkEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1))
v5LinkEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:v5LinkEntry.setStatus(_A)
_V5LinkV5IID_Type=Unsigned32
_V5LinkV5IID_Object=MibTableColumn
v5LinkV5IID=_V5LinkV5IID_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,1),_V5LinkV5IID_Type())
v5LinkV5IID.setMaxAccess(_F)
if mibBuilder.loadTexts:v5LinkV5IID.setStatus(_A)
class _V5LinkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_V5LinkID_Type.__name__=_B
_V5LinkID_Object=MibTableColumn
v5LinkID=_V5LinkID_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,2),_V5LinkID_Type())
v5LinkID.setMaxAccess(_F)
if mibBuilder.loadTexts:v5LinkID.setStatus(_A)
class _V5LinkRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_V5LinkRack_Type.__name__=_B
_V5LinkRack_Object=MibTableColumn
v5LinkRack=_V5LinkRack_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,3),_V5LinkRack_Type())
v5LinkRack.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LinkRack.setStatus(_A)
class _V5LinkShelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_V5LinkShelf_Type.__name__=_B
_V5LinkShelf_Object=MibTableColumn
v5LinkShelf=_V5LinkShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,4),_V5LinkShelf_Type())
v5LinkShelf.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LinkShelf.setStatus(_A)
class _V5LinkSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_V5LinkSlot_Type.__name__=_B
_V5LinkSlot_Object=MibTableColumn
v5LinkSlot=_V5LinkSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,5),_V5LinkSlot_Type())
v5LinkSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LinkSlot.setStatus(_A)
class _V5LinkE1No_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_V5LinkE1No_Type.__name__=_B
_V5LinkE1No_Object=MibTableColumn
v5LinkE1No=_V5LinkE1No_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,6),_V5LinkE1No_Type())
v5LinkE1No.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LinkE1No.setStatus(_A)
class _V5LinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('mainLink',0),('standbyLink',1),('normalLink',2)))
_V5LinkType_Type.__name__=_B
_V5LinkType_Object=MibTableColumn
v5LinkType=_V5LinkType_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,7),_V5LinkType_Type())
v5LinkType.setMaxAccess(_D)
if mibBuilder.loadTexts:v5LinkType.setStatus(_A)
class _V5LinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('linkNormal',0),('linkFault',1),('linkFaultBlock',2),('linkRemoteBlock',3),('linkLocalBlock',4),('linkCicBlock',5),('linkBlock',6)))
_V5LinkStatus_Type.__name__=_B
_V5LinkStatus_Object=MibTableColumn
v5LinkStatus=_V5LinkStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,8),_V5LinkStatus_Type())
v5LinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:v5LinkStatus.setStatus(_A)
class _V5LinkTs15PchFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('tsUnsed',1)))
_V5LinkTs15PchFlag_Type.__name__=_B
_V5LinkTs15PchFlag_Object=MibTableColumn
v5LinkTs15PchFlag=_V5LinkTs15PchFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,9),_V5LinkTs15PchFlag_Type())
v5LinkTs15PchFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:v5LinkTs15PchFlag.setStatus(_A)
class _V5LinkTs16PchFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_Q,1)))
_V5LinkTs16PchFlag_Type.__name__=_B
_V5LinkTs16PchFlag_Object=MibTableColumn
v5LinkTs16PchFlag=_V5LinkTs16PchFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,10),_V5LinkTs16PchFlag_Type())
v5LinkTs16PchFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:v5LinkTs16PchFlag.setStatus(_A)
class _V5LinkTs31PchFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_Q,1)))
_V5LinkTs31PchFlag_Type.__name__=_B
_V5LinkTs31PchFlag_Object=MibTableColumn
v5LinkTs31PchFlag=_V5LinkTs31PchFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,11),_V5LinkTs31PchFlag_Type())
v5LinkTs31PchFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:v5LinkTs31PchFlag.setStatus(_A)
class _V5LinkNewID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_V5LinkNewID_Type.__name__=_B
_V5LinkNewID_Object=MibTableColumn
v5LinkNewID=_V5LinkNewID_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,12),_V5LinkNewID_Type())
v5LinkNewID.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LinkNewID.setStatus(_A)
_V5LinkRowStatus_Type=RowStatus
_V5LinkRowStatus_Object=MibTableColumn
v5LinkRowStatus=_V5LinkRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,13),_V5LinkRowStatus_Type())
v5LinkRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LinkRowStatus.setStatus(_A)
class _V5linkBlockFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_V5linkBlockFlag_Type.__name__=_B
_V5linkBlockFlag_Object=MibTableColumn
v5linkBlockFlag=_V5linkBlockFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,14),_V5linkBlockFlag_Type())
v5linkBlockFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:v5linkBlockFlag.setStatus(_A)
class _V5linkVerify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_V5linkVerify_Type.__name__=_B
_V5linkVerify_Object=MibTableColumn
v5linkVerify=_V5linkVerify_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,15),_V5linkVerify_Type())
v5linkVerify.setMaxAccess(_C)
if mibBuilder.loadTexts:v5linkVerify.setStatus(_A)
class _V5linkTs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,31))
_V5linkTs_Type.__name__=_B
_V5linkTs_Object=MibTableColumn
v5linkTs=_V5linkTs_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,16),_V5linkTs_Type())
v5linkTs.setMaxAccess(_C)
if mibBuilder.loadTexts:v5linkTs.setStatus(_A)
class _V5linkAnfaultSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_V5linkAnfaultSet_Type.__name__=_B
_V5linkAnfaultSet_Object=MibTableColumn
v5linkAnfaultSet=_V5linkAnfaultSet_Object((1,3,6,1,4,1,3902,1015,5200,3,5,3,1,17),_V5linkAnfaultSet_Type())
v5linkAnfaultSet.setMaxAccess(_C)
if mibBuilder.loadTexts:v5linkAnfaultSet.setStatus(_A)
_V5PchTable_Object=MibTable
v5PchTable=_V5PchTable_Object((1,3,6,1,4,1,3902,1015,5200,3,5,5))
if mibBuilder.loadTexts:v5PchTable.setStatus(_A)
_V5PchEntry_Object=MibTableRow
v5PchEntry=_V5PchEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,5,5,1))
v5PchEntry.setIndexNames((0,_E,_R),(0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:v5PchEntry.setStatus(_A)
_V5PchV5IID_Type=Unsigned32
_V5PchV5IID_Object=MibTableColumn
v5PchV5IID=_V5PchV5IID_Object((1,3,6,1,4,1,3902,1015,5200,3,5,5,1,1),_V5PchV5IID_Type())
v5PchV5IID.setMaxAccess(_F)
if mibBuilder.loadTexts:v5PchV5IID.setStatus(_A)
class _V5PchLinkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_V5PchLinkId_Type.__name__=_B
_V5PchLinkId_Object=MibTableColumn
v5PchLinkId=_V5PchLinkId_Object((1,3,6,1,4,1,3902,1015,5200,3,5,5,1,2),_V5PchLinkId_Type())
v5PchLinkId.setMaxAccess(_F)
if mibBuilder.loadTexts:v5PchLinkId.setStatus(_A)
class _V5PchLinkTs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_V5PchLinkTs_Type.__name__=_B
_V5PchLinkTs_Object=MibTableColumn
v5PchLinkTs=_V5PchLinkTs_Object((1,3,6,1,4,1,3902,1015,5200,3,5,5,1,3),_V5PchLinkTs_Type())
v5PchLinkTs.setMaxAccess(_F)
if mibBuilder.loadTexts:v5PchLinkTs.setStatus(_A)
class _V5PchProtGrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_V5PchProtGrp_Type.__name__=_B
_V5PchProtGrp_Object=MibTableColumn
v5PchProtGrp=_V5PchProtGrp_Object((1,3,6,1,4,1,3902,1015,5200,3,5,5,1,4),_V5PchProtGrp_Type())
v5PchProtGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:v5PchProtGrp.setStatus(_A)
class _V5PchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('pchNormal',0),('pchAbNormal',1)))
_V5PchStatus_Type.__name__=_B
_V5PchStatus_Object=MibTableColumn
v5PchStatus=_V5PchStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,5,1,5),_V5PchStatus_Type())
v5PchStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:v5PchStatus.setStatus(_A)
_V5PchCtsTln_Type=Integer32
_V5PchCtsTln_Object=MibTableColumn
v5PchCtsTln=_V5PchCtsTln_Object((1,3,6,1,4,1,3902,1015,5200,3,5,5,1,6),_V5PchCtsTln_Type())
v5PchCtsTln.setMaxAccess(_D)
if mibBuilder.loadTexts:v5PchCtsTln.setStatus(_A)
_V5PchRowStatus_Type=RowStatus
_V5PchRowStatus_Object=MibTableColumn
v5PchRowStatus=_V5PchRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,5,1,7),_V5PchRowStatus_Type())
v5PchRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:v5PchRowStatus.setStatus(_A)
_V5LchTable_Object=MibTable
v5LchTable=_V5LchTable_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6))
if mibBuilder.loadTexts:v5LchTable.setStatus(_A)
_V5LchEntry_Object=MibTableRow
v5LchEntry=_V5LchEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1))
v5LchEntry.setIndexNames((0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:v5LchEntry.setStatus(_A)
class _V5LchV5IID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_V5LchV5IID_Type.__name__=_M
_V5LchV5IID_Object=MibTableColumn
v5LchV5IID=_V5LchV5IID_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,1),_V5LchV5IID_Type())
v5LchV5IID.setMaxAccess(_F)
if mibBuilder.loadTexts:v5LchV5IID.setStatus(_A)
class _V5LchLcci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_V5LchLcci_Type.__name__=_B
_V5LchLcci_Object=MibTableColumn
v5LchLcci=_V5LchLcci_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,2),_V5LchLcci_Type())
v5LchLcci.setMaxAccess(_F)
if mibBuilder.loadTexts:v5LchLcci.setStatus(_A)
class _V5LchLinkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_V5LchLinkID_Type.__name__=_B
_V5LchLinkID_Object=MibTableColumn
v5LchLinkID=_V5LchLinkID_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,3),_V5LchLinkID_Type())
v5LchLinkID.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LchLinkID.setStatus(_A)
class _V5LchLinkTs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_V5LchLinkTs_Type.__name__=_B
_V5LchLinkTs_Object=MibTableColumn
v5LchLinkTs=_V5LchLinkTs_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,4),_V5LchLinkTs_Type())
v5LchLinkTs.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LchLinkTs.setStatus(_A)
class _V5LchIsdnCreatedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_V5LchIsdnCreatedFlag_Type.__name__=_B
_V5LchIsdnCreatedFlag_Object=MibTableColumn
v5LchIsdnCreatedFlag=_V5LchIsdnCreatedFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,5),_V5LchIsdnCreatedFlag_Type())
v5LchIsdnCreatedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LchIsdnCreatedFlag.setStatus(_A)
class _V5LchPstnCrreatedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_V5LchPstnCrreatedFlag_Type.__name__=_B
_V5LchPstnCrreatedFlag_Object=MibTableColumn
v5LchPstnCrreatedFlag=_V5LchPstnCrreatedFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,6),_V5LchPstnCrreatedFlag_Type())
v5LchPstnCrreatedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LchPstnCrreatedFlag.setStatus(_A)
class _V5LchCtrlCreatedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_V5LchCtrlCreatedFlag_Type.__name__=_B
_V5LchCtrlCreatedFlag_Object=MibTableColumn
v5LchCtrlCreatedFlag=_V5LchCtrlCreatedFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,7),_V5LchCtrlCreatedFlag_Type())
v5LchCtrlCreatedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LchCtrlCreatedFlag.setStatus(_A)
class _V5LchBccCreatedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_V5LchBccCreatedFlag_Type.__name__=_B
_V5LchBccCreatedFlag_Object=MibTableColumn
v5LchBccCreatedFlag=_V5LchBccCreatedFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,8),_V5LchBccCreatedFlag_Type())
v5LchBccCreatedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LchBccCreatedFlag.setStatus(_A)
class _V5LchLinkCreatedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_V5LchLinkCreatedFlag_Type.__name__=_B
_V5LchLinkCreatedFlag_Object=MibTableColumn
v5LchLinkCreatedFlag=_V5LchLinkCreatedFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,9),_V5LchLinkCreatedFlag_Type())
v5LchLinkCreatedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LchLinkCreatedFlag.setStatus(_A)
class _V5LchProtCreatedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_V5LchProtCreatedFlag_Type.__name__=_B
_V5LchProtCreatedFlag_Object=MibTableColumn
v5LchProtCreatedFlag=_V5LchProtCreatedFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,10),_V5LchProtCreatedFlag_Type())
v5LchProtCreatedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LchProtCreatedFlag.setStatus(_A)
class _V5LchCurrLinkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_V5LchCurrLinkId_Type.__name__=_B
_V5LchCurrLinkId_Object=MibTableColumn
v5LchCurrLinkId=_V5LchCurrLinkId_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,11),_V5LchCurrLinkId_Type())
v5LchCurrLinkId.setMaxAccess(_D)
if mibBuilder.loadTexts:v5LchCurrLinkId.setStatus(_A)
class _V5LchCurrLinkTs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_V5LchCurrLinkTs_Type.__name__=_B
_V5LchCurrLinkTs_Object=MibTableColumn
v5LchCurrLinkTs=_V5LchCurrLinkTs_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,12),_V5LchCurrLinkTs_Type())
v5LchCurrLinkTs.setMaxAccess(_D)
if mibBuilder.loadTexts:v5LchCurrLinkTs.setStatus(_A)
class _V5LchSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noop',0),('switch',1)))
_V5LchSwitch_Type.__name__=_B
_V5LchSwitch_Object=MibTableColumn
v5LchSwitch=_V5LchSwitch_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,13),_V5LchSwitch_Type())
v5LchSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LchSwitch.setStatus(_A)
_V5LchRowStatus_Type=RowStatus
_V5LchRowStatus_Object=MibTableColumn
v5LchRowStatus=_V5LchRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,6,1,14),_V5LchRowStatus_Type())
v5LchRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:v5LchRowStatus.setStatus(_A)
_V5PstnUserTable_Object=MibTable
v5PstnUserTable=_V5PstnUserTable_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8))
if mibBuilder.loadTexts:v5PstnUserTable.setStatus(_A)
_V5PstnUserEntry_Object=MibTableRow
v5PstnUserEntry=_V5PstnUserEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1))
v5PstnUserEntry.setIndexNames((0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:v5PstnUserEntry.setStatus(_A)
_PstnV5IID_Type=Unsigned32
_PstnV5IID_Object=MibTableColumn
pstnV5IID=_PstnV5IID_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,1),_PstnV5IID_Type())
pstnV5IID.setMaxAccess(_F)
if mibBuilder.loadTexts:pstnV5IID.setStatus(_A)
class _PstnL3Addr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PstnL3Addr_Type.__name__=_B
_PstnL3Addr_Object=MibTableColumn
pstnL3Addr=_PstnL3Addr_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,2),_PstnL3Addr_Type())
pstnL3Addr.setMaxAccess(_F)
if mibBuilder.loadTexts:pstnL3Addr.setStatus(_A)
class _PstnRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_PstnRack_Type.__name__=_B
_PstnRack_Object=MibTableColumn
pstnRack=_PstnRack_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,3),_PstnRack_Type())
pstnRack.setMaxAccess(_C)
if mibBuilder.loadTexts:pstnRack.setStatus(_A)
class _PstnShelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_PstnShelf_Type.__name__=_B
_PstnShelf_Object=MibTableColumn
pstnShelf=_PstnShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,4),_PstnShelf_Type())
pstnShelf.setMaxAccess(_C)
if mibBuilder.loadTexts:pstnShelf.setStatus(_A)
class _PstnSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_PstnSlot_Type.__name__=_B
_PstnSlot_Object=MibTableColumn
pstnSlot=_PstnSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,5),_PstnSlot_Type())
pstnSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:pstnSlot.setStatus(_A)
class _PstnPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_PstnPort_Type.__name__=_B
_PstnPort_Object=MibTableColumn
pstnPort=_PstnPort_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,6),_PstnPort_Type())
pstnPort.setMaxAccess(_C)
if mibBuilder.loadTexts:pstnPort.setStatus(_A)
class _TrunkRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_TrunkRack_Type.__name__=_B
_TrunkRack_Object=MibTableColumn
trunkRack=_TrunkRack_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,7),_TrunkRack_Type())
trunkRack.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkRack.setStatus(_A)
class _TrunkShelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_TrunkShelf_Type.__name__=_B
_TrunkShelf_Object=MibTableColumn
trunkShelf=_TrunkShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,8),_TrunkShelf_Type())
trunkShelf.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkShelf.setStatus(_A)
class _TrunkSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,8),ValueRangeConstraint(11,12))
_TrunkSlot_Type.__name__=_B
_TrunkSlot_Object=MibTableColumn
trunkSlot=_TrunkSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,9),_TrunkSlot_Type())
trunkSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkSlot.setStatus(_A)
class _TrunkE1No_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_TrunkE1No_Type.__name__=_B
_TrunkE1No_Object=MibTableColumn
trunkE1No=_TrunkE1No_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,10),_TrunkE1No_Type())
trunkE1No.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkE1No.setStatus(_A)
class _TrunkCircuit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_TrunkCircuit_Type.__name__=_B
_TrunkCircuit_Object=MibTableColumn
trunkCircuit=_TrunkCircuit_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,11),_TrunkCircuit_Type())
trunkCircuit.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkCircuit.setStatus(_A)
class _PstnConnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fix',0),(_Y,1)))
_PstnConnType_Type.__name__=_B
_PstnConnType_Object=MibTableColumn
pstnConnType=_PstnConnType_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,12),_PstnConnType_Type())
pstnConnType.setMaxAccess(_C)
if mibBuilder.loadTexts:pstnConnType.setStatus(_A)
_PstnTelType_Type=Integer32
_PstnTelType_Object=MibTableColumn
pstnTelType=_PstnTelType_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,13),_PstnTelType_Type())
pstnTelType.setMaxAccess(_D)
if mibBuilder.loadTexts:pstnTelType.setStatus(_A)
class _PstnPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Z,0),(_a,1),(_b,2)))
_PstnPortStatus_Type.__name__=_B
_PstnPortStatus_Object=MibTableColumn
pstnPortStatus=_PstnPortStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,17),_PstnPortStatus_Type())
pstnPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pstnPortStatus.setStatus(_A)
class _PstnProtocolStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),(_d,1)))
_PstnProtocolStatus_Type.__name__=_B
_PstnProtocolStatus_Object=MibTableColumn
pstnProtocolStatus=_PstnProtocolStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,18),_PstnProtocolStatus_Type())
pstnProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pstnProtocolStatus.setStatus(_A)
class _PstnSum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,192))
_PstnSum_Type.__name__=_B
_PstnSum_Object=MibTableColumn
pstnSum=_PstnSum_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,25),_PstnSum_Type())
pstnSum.setMaxAccess(_C)
if mibBuilder.loadTexts:pstnSum.setStatus(_A)
_PstnRowStatus_Type=RowStatus
_PstnRowStatus_Object=MibTableColumn
pstnRowStatus=_PstnRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,26),_PstnRowStatus_Type())
pstnRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pstnRowStatus.setStatus(_A)
class _PstnportBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_PstnportBlock_Type.__name__=_B
_PstnportBlock_Object=MibTableColumn
pstnportBlock=_PstnportBlock_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,27),_PstnportBlock_Type())
pstnportBlock.setMaxAccess(_C)
if mibBuilder.loadTexts:pstnportBlock.setStatus(_A)
class _PstnportUnBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PstnportUnBlock_Type.__name__=_B
_PstnportUnBlock_Object=MibTableColumn
pstnportUnBlock=_PstnportUnBlock_Object((1,3,6,1,4,1,3902,1015,5200,3,5,8,1,28),_PstnportUnBlock_Type())
pstnportUnBlock.setMaxAccess(_C)
if mibBuilder.loadTexts:pstnportUnBlock.setStatus(_A)
_V5IsdnUserTable_Object=MibTable
v5IsdnUserTable=_V5IsdnUserTable_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9))
if mibBuilder.loadTexts:v5IsdnUserTable.setStatus(_A)
_V5IsdnUserEntry_Object=MibTableRow
v5IsdnUserEntry=_V5IsdnUserEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1))
v5IsdnUserEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:v5IsdnUserEntry.setStatus(_A)
_IsdnV5IID_Type=Unsigned32
_IsdnV5IID_Object=MibTableColumn
isdnV5IID=_IsdnV5IID_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,1),_IsdnV5IID_Type())
isdnV5IID.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnV5IID.setStatus(_A)
class _IsdnEfAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_IsdnEfAddr_Type.__name__=_B
_IsdnEfAddr_Object=MibTableColumn
isdnEfAddr=_IsdnEfAddr_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,2),_IsdnEfAddr_Type())
isdnEfAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:isdnEfAddr.setStatus(_A)
class _IsdnRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_IsdnRack_Type.__name__=_B
_IsdnRack_Object=MibTableColumn
isdnRack=_IsdnRack_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,3),_IsdnRack_Type())
isdnRack.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnRack.setStatus(_A)
class _IsdnShelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_IsdnShelf_Type.__name__=_B
_IsdnShelf_Object=MibTableColumn
isdnShelf=_IsdnShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,4),_IsdnShelf_Type())
isdnShelf.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnShelf.setStatus(_A)
class _IsdnSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_IsdnSlot_Type.__name__=_B
_IsdnSlot_Object=MibTableColumn
isdnSlot=_IsdnSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,5),_IsdnSlot_Type())
isdnSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnSlot.setStatus(_A)
class _IsdnPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_IsdnPort_Type.__name__=_B
_IsdnPort_Object=MibTableColumn
isdnPort=_IsdnPort_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,6),_IsdnPort_Type())
isdnPort.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnPort.setStatus(_A)
class _IsdnTrunkRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_IsdnTrunkRack_Type.__name__=_B
_IsdnTrunkRack_Object=MibTableColumn
isdnTrunkRack=_IsdnTrunkRack_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,7),_IsdnTrunkRack_Type())
isdnTrunkRack.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnTrunkRack.setStatus(_A)
class _IsdnTrunkShelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_IsdnTrunkShelf_Type.__name__=_B
_IsdnTrunkShelf_Object=MibTableColumn
isdnTrunkShelf=_IsdnTrunkShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,8),_IsdnTrunkShelf_Type())
isdnTrunkShelf.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnTrunkShelf.setStatus(_A)
class _IsdnTrunkSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,8),ValueRangeConstraint(11,12))
_IsdnTrunkSlot_Type.__name__=_B
_IsdnTrunkSlot_Object=MibTableColumn
isdnTrunkSlot=_IsdnTrunkSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,9),_IsdnTrunkSlot_Type())
isdnTrunkSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnTrunkSlot.setStatus(_A)
class _IsdnTrunkE1No_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_IsdnTrunkE1No_Type.__name__=_B
_IsdnTrunkE1No_Object=MibTableColumn
isdnTrunkE1No=_IsdnTrunkE1No_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,10),_IsdnTrunkE1No_Type())
isdnTrunkE1No.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnTrunkE1No.setStatus(_A)
class _IsdnTrunkCircuit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_IsdnTrunkCircuit_Type.__name__=_B
_IsdnTrunkCircuit_Object=MibTableColumn
isdnTrunkCircuit=_IsdnTrunkCircuit_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,11),_IsdnTrunkCircuit_Type())
isdnTrunkCircuit.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnTrunkCircuit.setStatus(_A)
class _IsdnConnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fix',0),(_Y,1)))
_IsdnConnType_Type.__name__=_B
_IsdnConnType_Object=MibTableColumn
isdnConnType=_IsdnConnType_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,12),_IsdnConnType_Type())
isdnConnType.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnConnType.setStatus(_A)
_IsdnTelType_Type=Integer32
_IsdnTelType_Object=MibTableColumn
isdnTelType=_IsdnTelType_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,13),_IsdnTelType_Type())
isdnTelType.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnTelType.setStatus(_A)
class _IsdnDsLcci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_IsdnDsLcci_Type.__name__=_B
_IsdnDsLcci_Object=MibTableColumn
isdnDsLcci=_IsdnDsLcci_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,14),_IsdnDsLcci_Type())
isdnDsLcci.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnDsLcci.setStatus(_A)
class _IsdnGroupLcci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_IsdnGroupLcci_Type.__name__=_B
_IsdnGroupLcci_Object=MibTableColumn
isdnGroupLcci=_IsdnGroupLcci_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,15),_IsdnGroupLcci_Type())
isdnGroupLcci.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnGroupLcci.setStatus(_A)
class _IsdnFrameLcci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_IsdnFrameLcci_Type.__name__=_B
_IsdnFrameLcci_Object=MibTableColumn
isdnFrameLcci=_IsdnFrameLcci_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,16),_IsdnFrameLcci_Type())
isdnFrameLcci.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnFrameLcci.setStatus(_A)
class _IsdnPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Z,0),(_a,1),(_b,2)))
_IsdnPortStatus_Type.__name__=_B
_IsdnPortStatus_Object=MibTableColumn
isdnPortStatus=_IsdnPortStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,17),_IsdnPortStatus_Type())
isdnPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnPortStatus.setStatus(_A)
class _IsdnProtocolStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),(_d,1)))
_IsdnProtocolStatus_Type.__name__=_B
_IsdnProtocolStatus_Object=MibTableColumn
isdnProtocolStatus=_IsdnProtocolStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,18),_IsdnProtocolStatus_Type())
isdnProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnProtocolStatus.setStatus(_A)
class _IsdnSemiPermFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('flagUsed',0),('flagUnused',1)))
_IsdnSemiPermFlag_Type.__name__=_B
_IsdnSemiPermFlag_Object=MibTableColumn
isdnSemiPermFlag=_IsdnSemiPermFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,19),_IsdnSemiPermFlag_Type())
isdnSemiPermFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnSemiPermFlag.setStatus(_A)
class _IsdnPolarityFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('positive',0),('negative',1)))
_IsdnPolarityFlag_Type.__name__=_B
_IsdnPolarityFlag_Object=MibTableColumn
isdnPolarityFlag=_IsdnPolarityFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,20),_IsdnPolarityFlag_Type())
isdnPolarityFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnPolarityFlag.setStatus(_A)
_IsdnDistance_Type=Integer32
_IsdnDistance_Object=MibTableColumn
isdnDistance=_IsdnDistance_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,21),_IsdnDistance_Type())
isdnDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnDistance.setStatus(_A)
_IsdnV51UpPir_Type=Integer32
_IsdnV51UpPir_Object=MibTableColumn
isdnV51UpPir=_IsdnV51UpPir_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,22),_IsdnV51UpPir_Type())
isdnV51UpPir.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnV51UpPir.setStatus(_A)
_IsdnV52UpPir_Type=Integer32
_IsdnV52UpPir_Object=MibTableColumn
isdnV52UpPir=_IsdnV52UpPir_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,23),_IsdnV52UpPir_Type())
isdnV52UpPir.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnV52UpPir.setStatus(_A)
_IsdnV5IsAnfault_Type=Integer32
_IsdnV5IsAnfault_Object=MibTableColumn
isdnV5IsAnfault=_IsdnV5IsAnfault_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,24),_IsdnV5IsAnfault_Type())
isdnV5IsAnfault.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnV5IsAnfault.setStatus(_A)
class _IsdnSum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,192))
_IsdnSum_Type.__name__=_B
_IsdnSum_Object=MibTableColumn
isdnSum=_IsdnSum_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,25),_IsdnSum_Type())
isdnSum.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnSum.setStatus(_A)
_IsdnRowStatus_Type=RowStatus
_IsdnRowStatus_Object=MibTableColumn
isdnRowStatus=_IsdnRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,26),_IsdnRowStatus_Type())
isdnRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnRowStatus.setStatus(_A)
class _IsdnActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_IsdnActive_Type.__name__=_B
_IsdnActive_Object=MibTableColumn
isdnActive=_IsdnActive_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,27),_IsdnActive_Type())
isdnActive.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnActive.setStatus(_A)
class _IsdnBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_IsdnBlock_Type.__name__=_B
_IsdnBlock_Object=MibTableColumn
isdnBlock=_IsdnBlock_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,28),_IsdnBlock_Type())
isdnBlock.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnBlock.setStatus(_A)
class _IsdnUnBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_IsdnUnBlock_Type.__name__=_B
_IsdnUnBlock_Object=MibTableColumn
isdnUnBlock=_IsdnUnBlock_Object((1,3,6,1,4,1,3902,1015,5200,3,5,9,1,29),_IsdnUnBlock_Type())
isdnUnBlock.setMaxAccess(_C)
if mibBuilder.loadTexts:isdnUnBlock.setStatus(_A)
class _MsagServiceV5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notSupport',0),('support',1)))
_MsagServiceV5_Type.__name__=_B
_MsagServiceV5_Object=MibScalar
msagServiceV5=_MsagServiceV5_Object((1,3,6,1,4,1,3902,1015,5200,3,5,10),_MsagServiceV5_Type())
msagServiceV5.setMaxAccess(_D)
if mibBuilder.loadTexts:msagServiceV5.setStatus(_A)
_V5LinkTsTable_Object=MibTable
v5LinkTsTable=_V5LinkTsTable_Object((1,3,6,1,4,1,3902,1015,5200,3,5,11))
if mibBuilder.loadTexts:v5LinkTsTable.setStatus(_A)
_V5LinkTsEntry_Object=MibTableRow
v5LinkTsEntry=_V5LinkTsEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,5,11,1))
v5LinkTsEntry.setIndexNames((0,_E,_g),(0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:v5LinkTsEntry.setStatus(_A)
_V5LinkTsV5IID_Type=Unsigned32
_V5LinkTsV5IID_Object=MibTableColumn
v5LinkTsV5IID=_V5LinkTsV5IID_Object((1,3,6,1,4,1,3902,1015,5200,3,5,11,1,1),_V5LinkTsV5IID_Type())
v5LinkTsV5IID.setMaxAccess(_F)
if mibBuilder.loadTexts:v5LinkTsV5IID.setStatus(_A)
class _V5LinkTsLinkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_V5LinkTsLinkID_Type.__name__=_B
_V5LinkTsLinkID_Object=MibTableColumn
v5LinkTsLinkID=_V5LinkTsLinkID_Object((1,3,6,1,4,1,3902,1015,5200,3,5,11,1,2),_V5LinkTsLinkID_Type())
v5LinkTsLinkID.setMaxAccess(_F)
if mibBuilder.loadTexts:v5LinkTsLinkID.setStatus(_A)
class _V5LinkTsNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_V5LinkTsNo_Type.__name__=_B
_V5LinkTsNo_Object=MibTableColumn
v5LinkTsNo=_V5LinkTsNo_Object((1,3,6,1,4,1,3902,1015,5200,3,5,11,1,3),_V5LinkTsNo_Type())
v5LinkTsNo.setMaxAccess(_F)
if mibBuilder.loadTexts:v5LinkTsNo.setStatus(_A)
class _V5LinkTsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,255)));namedValues=NamedValues(*(('tlnidle',0),('tlnbusy',1),('tlnblock',2),('tlninvalid',255)))
_V5LinkTsState_Type.__name__=_B
_V5LinkTsState_Object=MibTableColumn
v5LinkTsState=_V5LinkTsState_Object((1,3,6,1,4,1,3902,1015,5200,3,5,11,1,4),_V5LinkTsState_Type())
v5LinkTsState.setMaxAccess(_D)
if mibBuilder.loadTexts:v5LinkTsState.setStatus(_A)
class _V5LinkTsL3Addr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_V5LinkTsL3Addr_Type.__name__=_B
_V5LinkTsL3Addr_Object=MibTableColumn
v5LinkTsL3Addr=_V5LinkTsL3Addr_Object((1,3,6,1,4,1,3902,1015,5200,3,5,11,1,5),_V5LinkTsL3Addr_Type())
v5LinkTsL3Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:v5LinkTsL3Addr.setStatus(_A)
class _V5LinkTsFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_V5LinkTsFlag_Type.__name__=_B
_V5LinkTsFlag_Object=MibTableColumn
v5LinkTsFlag=_V5LinkTsFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,5,11,1,6),_V5LinkTsFlag_Type())
v5LinkTsFlag.setMaxAccess(_L)
if mibBuilder.loadTexts:v5LinkTsFlag.setStatus(_A)
class _V5LinkTsBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_V5LinkTsBlock_Type.__name__=_B
_V5LinkTsBlock_Object=MibTableColumn
v5LinkTsBlock=_V5LinkTsBlock_Object((1,3,6,1,4,1,3902,1015,5200,3,5,11,1,7),_V5LinkTsBlock_Type())
v5LinkTsBlock.setMaxAccess(_L)
if mibBuilder.loadTexts:v5LinkTsBlock.setStatus(_A)
class _V5LinkTsUnBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_V5LinkTsUnBlock_Type.__name__=_B
_V5LinkTsUnBlock_Object=MibTableColumn
v5LinkTsUnBlock=_V5LinkTsUnBlock_Object((1,3,6,1,4,1,3902,1015,5200,3,5,11,1,8),_V5LinkTsUnBlock_Type())
v5LinkTsUnBlock.setMaxAccess(_L)
if mibBuilder.loadTexts:v5LinkTsUnBlock.setStatus(_A)
_ZxAnV5UaLinkTable_Object=MibTable
zxAnV5UaLinkTable=_ZxAnV5UaLinkTable_Object((1,3,6,1,4,1,3902,1015,5200,3,5,12))
if mibBuilder.loadTexts:zxAnV5UaLinkTable.setStatus(_A)
_ZxAnV5UaLinkEntry_Object=MibTableRow
zxAnV5UaLinkEntry=_ZxAnV5UaLinkEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,5,12,1))
zxAnV5UaLinkEntry.setIndexNames((0,_E,_j),(0,_E,_k),(0,_E,_l),(0,_E,_m),(0,_E,_n))
if mibBuilder.loadTexts:zxAnV5UaLinkEntry.setStatus(_A)
_ZxAnV5UaLinkRack_Type=Integer32
_ZxAnV5UaLinkRack_Object=MibTableColumn
zxAnV5UaLinkRack=_ZxAnV5UaLinkRack_Object((1,3,6,1,4,1,3902,1015,5200,3,5,12,1,1),_ZxAnV5UaLinkRack_Type())
zxAnV5UaLinkRack.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnV5UaLinkRack.setStatus(_A)
_ZxAnV5UaLinkShelf_Type=Integer32
_ZxAnV5UaLinkShelf_Object=MibTableColumn
zxAnV5UaLinkShelf=_ZxAnV5UaLinkShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,5,12,1,2),_ZxAnV5UaLinkShelf_Type())
zxAnV5UaLinkShelf.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnV5UaLinkShelf.setStatus(_A)
_ZxAnV5UaLinkSlot_Type=Integer32
_ZxAnV5UaLinkSlot_Object=MibTableColumn
zxAnV5UaLinkSlot=_ZxAnV5UaLinkSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,5,12,1,3),_ZxAnV5UaLinkSlot_Type())
zxAnV5UaLinkSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnV5UaLinkSlot.setStatus(_A)
class _ZxAnV5UaLinkDsx1LinkNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ZxAnV5UaLinkDsx1LinkNo_Type.__name__=_B
_ZxAnV5UaLinkDsx1LinkNo_Object=MibTableColumn
zxAnV5UaLinkDsx1LinkNo=_ZxAnV5UaLinkDsx1LinkNo_Object((1,3,6,1,4,1,3902,1015,5200,3,5,12,1,4),_ZxAnV5UaLinkDsx1LinkNo_Type())
zxAnV5UaLinkDsx1LinkNo.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnV5UaLinkDsx1LinkNo.setStatus(_A)
_ZxAnV5UaLinkDsx1TsNo_Type=Integer32
_ZxAnV5UaLinkDsx1TsNo_Object=MibTableColumn
zxAnV5UaLinkDsx1TsNo=_ZxAnV5UaLinkDsx1TsNo_Object((1,3,6,1,4,1,3902,1015,5200,3,5,12,1,5),_ZxAnV5UaLinkDsx1TsNo_Type())
zxAnV5UaLinkDsx1TsNo.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnV5UaLinkDsx1TsNo.setStatus(_A)
class _ZxAnV5UaLinkV5LinkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnV5UaLinkV5LinkId_Type.__name__=_B
_ZxAnV5UaLinkV5LinkId_Object=MibTableColumn
zxAnV5UaLinkV5LinkId=_ZxAnV5UaLinkV5LinkId_Object((1,3,6,1,4,1,3902,1015,5200,3,5,12,1,6),_ZxAnV5UaLinkV5LinkId_Type())
zxAnV5UaLinkV5LinkId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnV5UaLinkV5LinkId.setStatus(_A)
class _ZxAnV5UaLinkAsId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_ZxAnV5UaLinkAsId_Type.__name__=_B
_ZxAnV5UaLinkAsId_Object=MibTableColumn
zxAnV5UaLinkAsId=_ZxAnV5UaLinkAsId_Object((1,3,6,1,4,1,3902,1015,5200,3,5,12,1,7),_ZxAnV5UaLinkAsId_Type())
zxAnV5UaLinkAsId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnV5UaLinkAsId.setStatus(_A)
class _ZxAnV5UaLinkIfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_ZxAnV5UaLinkIfId_Type.__name__=_B
_ZxAnV5UaLinkIfId_Object=MibTableColumn
zxAnV5UaLinkIfId=_ZxAnV5UaLinkIfId_Object((1,3,6,1,4,1,3902,1015,5200,3,5,12,1,8),_ZxAnV5UaLinkIfId_Type())
zxAnV5UaLinkIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnV5UaLinkIfId.setStatus(_A)
_ZxAnV5UaLinkRowStatus_Type=RowStatus
_ZxAnV5UaLinkRowStatus_Object=MibTableColumn
zxAnV5UaLinkRowStatus=_ZxAnV5UaLinkRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,5,12,1,50),_ZxAnV5UaLinkRowStatus_Type())
zxAnV5UaLinkRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnV5UaLinkRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zte':zte,'zxAn':zxAn,'zxAnV5Mib':zxAnV5Mib,'msagmajorVersion':msagmajorVersion,'msagV5Service':msagV5Service,'v5InterfaceTable':v5InterfaceTable,'v5InterfaceEntry':v5InterfaceEntry,_N:v5IFID,'v5IFType':v5IFType,'v5IFVar':v5IFVar,'v5IFLeType':v5IFLeType,'v5IFStatus':v5IFStatus,'v5IFCommCtrlStatus':v5IFCommCtrlStatus,'v5IFPstnDLStatus':v5IFPstnDLStatus,'v5IFBccDLStatus':v5IFBccDLStatus,'v5IFLinkDLStatus':v5IFLinkDLStatus,'v5IFCtrlDLStatus':v5IFCtrlDLStatus,'v5IFProtMDLStatus':v5IFProtMDLStatus,'v5IFProtBDLStatus':v5IFProtBDLStatus,'v5IFNewV5IID':v5IFNewV5IID,'v5IFRowStatus':v5IFRowStatus,'v5LinkTable':v5LinkTable,'v5LinkEntry':v5LinkEntry,_O:v5LinkV5IID,_P:v5LinkID,'v5LinkRack':v5LinkRack,'v5LinkShelf':v5LinkShelf,'v5LinkSlot':v5LinkSlot,'v5LinkE1No':v5LinkE1No,'v5LinkType':v5LinkType,'v5LinkStatus':v5LinkStatus,'v5LinkTs15PchFlag':v5LinkTs15PchFlag,'v5LinkTs16PchFlag':v5LinkTs16PchFlag,'v5LinkTs31PchFlag':v5LinkTs31PchFlag,'v5LinkNewID':v5LinkNewID,'v5LinkRowStatus':v5LinkRowStatus,'v5linkBlockFlag':v5linkBlockFlag,'v5linkVerify':v5linkVerify,'v5linkTs':v5linkTs,'v5linkAnfaultSet':v5linkAnfaultSet,'v5PchTable':v5PchTable,'v5PchEntry':v5PchEntry,_R:v5PchV5IID,_S:v5PchLinkId,_T:v5PchLinkTs,'v5PchProtGrp':v5PchProtGrp,'v5PchStatus':v5PchStatus,'v5PchCtsTln':v5PchCtsTln,'v5PchRowStatus':v5PchRowStatus,'v5LchTable':v5LchTable,'v5LchEntry':v5LchEntry,_U:v5LchV5IID,_V:v5LchLcci,'v5LchLinkID':v5LchLinkID,'v5LchLinkTs':v5LchLinkTs,'v5LchIsdnCreatedFlag':v5LchIsdnCreatedFlag,'v5LchPstnCrreatedFlag':v5LchPstnCrreatedFlag,'v5LchCtrlCreatedFlag':v5LchCtrlCreatedFlag,'v5LchBccCreatedFlag':v5LchBccCreatedFlag,'v5LchLinkCreatedFlag':v5LchLinkCreatedFlag,'v5LchProtCreatedFlag':v5LchProtCreatedFlag,'v5LchCurrLinkId':v5LchCurrLinkId,'v5LchCurrLinkTs':v5LchCurrLinkTs,'v5LchSwitch':v5LchSwitch,'v5LchRowStatus':v5LchRowStatus,'v5PstnUserTable':v5PstnUserTable,'v5PstnUserEntry':v5PstnUserEntry,_W:pstnV5IID,_X:pstnL3Addr,'pstnRack':pstnRack,'pstnShelf':pstnShelf,'pstnSlot':pstnSlot,'pstnPort':pstnPort,'trunkRack':trunkRack,'trunkShelf':trunkShelf,'trunkSlot':trunkSlot,'trunkE1No':trunkE1No,'trunkCircuit':trunkCircuit,'pstnConnType':pstnConnType,'pstnTelType':pstnTelType,'pstnPortStatus':pstnPortStatus,'pstnProtocolStatus':pstnProtocolStatus,'pstnSum':pstnSum,'pstnRowStatus':pstnRowStatus,'pstnportBlock':pstnportBlock,'pstnportUnBlock':pstnportUnBlock,'v5IsdnUserTable':v5IsdnUserTable,'v5IsdnUserEntry':v5IsdnUserEntry,_e:isdnV5IID,_f:isdnEfAddr,'isdnRack':isdnRack,'isdnShelf':isdnShelf,'isdnSlot':isdnSlot,'isdnPort':isdnPort,'isdnTrunkRack':isdnTrunkRack,'isdnTrunkShelf':isdnTrunkShelf,'isdnTrunkSlot':isdnTrunkSlot,'isdnTrunkE1No':isdnTrunkE1No,'isdnTrunkCircuit':isdnTrunkCircuit,'isdnConnType':isdnConnType,'isdnTelType':isdnTelType,'isdnDsLcci':isdnDsLcci,'isdnGroupLcci':isdnGroupLcci,'isdnFrameLcci':isdnFrameLcci,'isdnPortStatus':isdnPortStatus,'isdnProtocolStatus':isdnProtocolStatus,'isdnSemiPermFlag':isdnSemiPermFlag,'isdnPolarityFlag':isdnPolarityFlag,'isdnDistance':isdnDistance,'isdnV51UpPir':isdnV51UpPir,'isdnV52UpPir':isdnV52UpPir,'isdnV5IsAnfault':isdnV5IsAnfault,'isdnSum':isdnSum,'isdnRowStatus':isdnRowStatus,'isdnActive':isdnActive,'isdnBlock':isdnBlock,'isdnUnBlock':isdnUnBlock,'msagServiceV5':msagServiceV5,'v5LinkTsTable':v5LinkTsTable,'v5LinkTsEntry':v5LinkTsEntry,_g:v5LinkTsV5IID,_h:v5LinkTsLinkID,_i:v5LinkTsNo,'v5LinkTsState':v5LinkTsState,'v5LinkTsL3Addr':v5LinkTsL3Addr,'v5LinkTsFlag':v5LinkTsFlag,'v5LinkTsBlock':v5LinkTsBlock,'v5LinkTsUnBlock':v5LinkTsUnBlock,'zxAnV5UaLinkTable':zxAnV5UaLinkTable,'zxAnV5UaLinkEntry':zxAnV5UaLinkEntry,_j:zxAnV5UaLinkRack,_k:zxAnV5UaLinkShelf,_l:zxAnV5UaLinkSlot,_m:zxAnV5UaLinkDsx1LinkNo,_n:zxAnV5UaLinkDsx1TsNo,'zxAnV5UaLinkV5LinkId':zxAnV5UaLinkV5LinkId,'zxAnV5UaLinkAsId':zxAnV5UaLinkAsId,'zxAnV5UaLinkIfId':zxAnV5UaLinkIfId,'zxAnV5UaLinkRowStatus':zxAnV5UaLinkRowStatus})