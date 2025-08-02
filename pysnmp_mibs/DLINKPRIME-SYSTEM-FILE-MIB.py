_f='dpsfClearCfgGroup'
_e='dpsfCfgReplaceGroup'
_d='dpsfCopyGroup'
_c='dpsfBootInfoGroup'
_b='dpsfResetSystem'
_a='dpsfClearRunCfg'
_Z='dpsfCfgReplaceRowStatus'
_Y='dpsfCfgReplaceErrorStatus'
_X='dpsfCfgReplaceRemoteAddr'
_W='dpsfCfgReplaceSrcUrl'
_V='dpsfCfgReplaceSrcType'
_U='dpsfCopyRowStatus'
_T='dpsfCopyErrorStatus'
_S='dpsfCopyRemoteAddr'
_R='dpsfCopyDstUrl'
_Q='dpsfCopySrcUrl'
_P='dpsfCopyType'
_O='dpsfBootImageInWorking'
_N='dpsfBootImageCheckResult'
_M='dpsfCheckingBootImageCheck'
_L='dpsfCfgReplaceIndex'
_K='dpsfCopyIndex'
_J='dpsfBootImageIndex'
_I='not-accessible'
_H='read-write'
_G='Unsigned32'
_F='OctetString'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='DLINKPRIME-SYSTEM-FILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
dlinkPrimeSystemFileMIB=ModuleIdentity((1,3,6,1,4,1,171,15,22))
if mibBuilder.loadTexts:dlinkPrimeSystemFileMIB.setRevisions(('2014-05-26 00:00',))
_DpsfMIBNotifications_ObjectIdentity=ObjectIdentity
dpsfMIBNotifications=_DpsfMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,22,0))
_DpsfMIBObjects_ObjectIdentity=ObjectIdentity
dpsfMIBObjects=_DpsfMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,22,1))
_DpsfBootInfoObjects_ObjectIdentity=ObjectIdentity
dpsfBootInfoObjects=_DpsfBootInfoObjects_ObjectIdentity((1,3,6,1,4,1,171,15,22,1,1))
_DpsfCheckingBootImageCheck_Type=TruthValue
_DpsfCheckingBootImageCheck_Object=MibScalar
dpsfCheckingBootImageCheck=_DpsfCheckingBootImageCheck_Object((1,3,6,1,4,1,171,15,22,1,1,1),_DpsfCheckingBootImageCheck_Type())
dpsfCheckingBootImageCheck.setMaxAccess(_H)
if mibBuilder.loadTexts:dpsfCheckingBootImageCheck.setStatus(_A)
_DpsfBootImageCheckResult_Type=DisplayString
_DpsfBootImageCheckResult_Object=MibScalar
dpsfBootImageCheckResult=_DpsfBootImageCheckResult_Object((1,3,6,1,4,1,171,15,22,1,1,2),_DpsfBootImageCheckResult_Type())
dpsfBootImageCheckResult.setMaxAccess(_E)
if mibBuilder.loadTexts:dpsfBootImageCheckResult.setStatus(_A)
_DpsfBootImageTable_Object=MibTable
dpsfBootImageTable=_DpsfBootImageTable_Object((1,3,6,1,4,1,171,15,22,1,1,3))
if mibBuilder.loadTexts:dpsfBootImageTable.setStatus(_A)
_DpsfBootImageEntry_Object=MibTableRow
dpsfBootImageEntry=_DpsfBootImageEntry_Object((1,3,6,1,4,1,171,15,22,1,1,3,1))
dpsfBootImageEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:dpsfBootImageEntry.setStatus(_A)
class _DpsfBootImageIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DpsfBootImageIndex_Type.__name__=_G
_DpsfBootImageIndex_Object=MibTableColumn
dpsfBootImageIndex=_DpsfBootImageIndex_Object((1,3,6,1,4,1,171,15,22,1,1,3,1,1),_DpsfBootImageIndex_Type())
dpsfBootImageIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:dpsfBootImageIndex.setStatus(_A)
_DpsfBootImageInWorking_Type=TruthValue
_DpsfBootImageInWorking_Object=MibTableColumn
dpsfBootImageInWorking=_DpsfBootImageInWorking_Object((1,3,6,1,4,1,171,15,22,1,1,3,1,2),_DpsfBootImageInWorking_Type())
dpsfBootImageInWorking.setMaxAccess(_E)
if mibBuilder.loadTexts:dpsfBootImageInWorking.setStatus(_A)
_DpsfCopyTable_Object=MibTable
dpsfCopyTable=_DpsfCopyTable_Object((1,3,6,1,4,1,171,15,22,1,2))
if mibBuilder.loadTexts:dpsfCopyTable.setStatus(_A)
_DpsfCopyEntry_Object=MibTableRow
dpsfCopyEntry=_DpsfCopyEntry_Object((1,3,6,1,4,1,171,15,22,1,2,1))
dpsfCopyEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:dpsfCopyEntry.setStatus(_A)
class _DpsfCopyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_DpsfCopyIndex_Type.__name__=_G
_DpsfCopyIndex_Object=MibTableColumn
dpsfCopyIndex=_DpsfCopyIndex_Object((1,3,6,1,4,1,171,15,22,1,2,1,1),_DpsfCopyIndex_Type())
dpsfCopyIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:dpsfCopyIndex.setStatus(_A)
class _DpsfCopyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('localToTftpRemote',1),('tftpRemoteToLocal',2)))
_DpsfCopyType_Type.__name__=_D
_DpsfCopyType_Object=MibTableColumn
dpsfCopyType=_DpsfCopyType_Object((1,3,6,1,4,1,171,15,22,1,2,1,2),_DpsfCopyType_Type())
dpsfCopyType.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsfCopyType.setStatus(_A)
class _DpsfCopySrcUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,799))
_DpsfCopySrcUrl_Type.__name__=_F
_DpsfCopySrcUrl_Object=MibTableColumn
dpsfCopySrcUrl=_DpsfCopySrcUrl_Object((1,3,6,1,4,1,171,15,22,1,2,1,3),_DpsfCopySrcUrl_Type())
dpsfCopySrcUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsfCopySrcUrl.setStatus(_A)
class _DpsfCopyDstUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,799))
_DpsfCopyDstUrl_Type.__name__=_F
_DpsfCopyDstUrl_Object=MibTableColumn
dpsfCopyDstUrl=_DpsfCopyDstUrl_Object((1,3,6,1,4,1,171,15,22,1,2,1,4),_DpsfCopyDstUrl_Type())
dpsfCopyDstUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsfCopyDstUrl.setStatus(_A)
_DpsfCopyRemoteAddr_Type=IpAddress
_DpsfCopyRemoteAddr_Object=MibTableColumn
dpsfCopyRemoteAddr=_DpsfCopyRemoteAddr_Object((1,3,6,1,4,1,171,15,22,1,2,1,5),_DpsfCopyRemoteAddr_Type())
dpsfCopyRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsfCopyRemoteAddr.setStatus(_A)
_DpsfCopyErrorStatus_Type=DisplayString
_DpsfCopyErrorStatus_Object=MibTableColumn
dpsfCopyErrorStatus=_DpsfCopyErrorStatus_Object((1,3,6,1,4,1,171,15,22,1,2,1,6),_DpsfCopyErrorStatus_Type())
dpsfCopyErrorStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dpsfCopyErrorStatus.setStatus(_A)
_DpsfCopyRowStatus_Type=RowStatus
_DpsfCopyRowStatus_Object=MibTableColumn
dpsfCopyRowStatus=_DpsfCopyRowStatus_Object((1,3,6,1,4,1,171,15,22,1,2,1,7),_DpsfCopyRowStatus_Type())
dpsfCopyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsfCopyRowStatus.setStatus(_A)
_DpsfCfgReplaceTable_Object=MibTable
dpsfCfgReplaceTable=_DpsfCfgReplaceTable_Object((1,3,6,1,4,1,171,15,22,1,3))
if mibBuilder.loadTexts:dpsfCfgReplaceTable.setStatus(_A)
_DpsfCfgReplaceEntry_Object=MibTableRow
dpsfCfgReplaceEntry=_DpsfCfgReplaceEntry_Object((1,3,6,1,4,1,171,15,22,1,3,1))
dpsfCfgReplaceEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:dpsfCfgReplaceEntry.setStatus(_A)
class _DpsfCfgReplaceIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_DpsfCfgReplaceIndex_Type.__name__=_G
_DpsfCfgReplaceIndex_Object=MibTableColumn
dpsfCfgReplaceIndex=_DpsfCfgReplaceIndex_Object((1,3,6,1,4,1,171,15,22,1,3,1,1),_DpsfCfgReplaceIndex_Type())
dpsfCfgReplaceIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:dpsfCfgReplaceIndex.setStatus(_A)
class _DpsfCfgReplaceSrcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('tftpRemote',1))
_DpsfCfgReplaceSrcType_Type.__name__=_D
_DpsfCfgReplaceSrcType_Object=MibTableColumn
dpsfCfgReplaceSrcType=_DpsfCfgReplaceSrcType_Object((1,3,6,1,4,1,171,15,22,1,3,1,2),_DpsfCfgReplaceSrcType_Type())
dpsfCfgReplaceSrcType.setMaxAccess(_E)
if mibBuilder.loadTexts:dpsfCfgReplaceSrcType.setStatus(_A)
class _DpsfCfgReplaceSrcUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,799))
_DpsfCfgReplaceSrcUrl_Type.__name__=_F
_DpsfCfgReplaceSrcUrl_Object=MibTableColumn
dpsfCfgReplaceSrcUrl=_DpsfCfgReplaceSrcUrl_Object((1,3,6,1,4,1,171,15,22,1,3,1,3),_DpsfCfgReplaceSrcUrl_Type())
dpsfCfgReplaceSrcUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsfCfgReplaceSrcUrl.setStatus(_A)
_DpsfCfgReplaceRemoteAddr_Type=IpAddress
_DpsfCfgReplaceRemoteAddr_Object=MibTableColumn
dpsfCfgReplaceRemoteAddr=_DpsfCfgReplaceRemoteAddr_Object((1,3,6,1,4,1,171,15,22,1,3,1,4),_DpsfCfgReplaceRemoteAddr_Type())
dpsfCfgReplaceRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsfCfgReplaceRemoteAddr.setStatus(_A)
_DpsfCfgReplaceErrorStatus_Type=DisplayString
_DpsfCfgReplaceErrorStatus_Object=MibTableColumn
dpsfCfgReplaceErrorStatus=_DpsfCfgReplaceErrorStatus_Object((1,3,6,1,4,1,171,15,22,1,3,1,5),_DpsfCfgReplaceErrorStatus_Type())
dpsfCfgReplaceErrorStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dpsfCfgReplaceErrorStatus.setStatus(_A)
_DpsfCfgReplaceRowStatus_Type=RowStatus
_DpsfCfgReplaceRowStatus_Object=MibTableColumn
dpsfCfgReplaceRowStatus=_DpsfCfgReplaceRowStatus_Object((1,3,6,1,4,1,171,15,22,1,3,1,6),_DpsfCfgReplaceRowStatus_Type())
dpsfCfgReplaceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsfCfgReplaceRowStatus.setStatus(_A)
class _DpsfClearRunCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('clear_cfg_ip_reboot',1),('clear_cfg_no_ip_reboot',2),('clear_cfg_no_reboot',3),('noOp',4)))
_DpsfClearRunCfg_Type.__name__=_D
_DpsfClearRunCfg_Object=MibScalar
dpsfClearRunCfg=_DpsfClearRunCfg_Object((1,3,6,1,4,1,171,15,22,1,4),_DpsfClearRunCfg_Type())
dpsfClearRunCfg.setMaxAccess(_H)
if mibBuilder.loadTexts:dpsfClearRunCfg.setStatus(_A)
class _DpsfResetSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),('noOp',2)))
_DpsfResetSystem_Type.__name__=_D
_DpsfResetSystem_Object=MibScalar
dpsfResetSystem=_DpsfResetSystem_Object((1,3,6,1,4,1,171,15,22,1,5),_DpsfResetSystem_Type())
dpsfResetSystem.setMaxAccess(_H)
if mibBuilder.loadTexts:dpsfResetSystem.setStatus(_A)
_DpsfMIBConformance_ObjectIdentity=ObjectIdentity
dpsfMIBConformance=_DpsfMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,22,2))
_DpsfCompliances_ObjectIdentity=ObjectIdentity
dpsfCompliances=_DpsfCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,22,2,1))
_DpsfGroups_ObjectIdentity=ObjectIdentity
dpsfGroups=_DpsfGroups_ObjectIdentity((1,3,6,1,4,1,171,15,22,2,2))
dpsfBootInfoGroup=ObjectGroup((1,3,6,1,4,1,171,15,22,2,2,1))
dpsfBootInfoGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:dpsfBootInfoGroup.setStatus(_A)
dpsfCopyGroup=ObjectGroup((1,3,6,1,4,1,171,15,22,2,2,2))
dpsfCopyGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:dpsfCopyGroup.setStatus(_A)
dpsfCfgReplaceGroup=ObjectGroup((1,3,6,1,4,1,171,15,22,2,2,3))
dpsfCfgReplaceGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:dpsfCfgReplaceGroup.setStatus(_A)
dpsfClearCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,22,2,2,4))
dpsfClearCfgGroup.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:dpsfClearCfgGroup.setStatus(_A)
dpsfCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,22,2,1,1))
dpsfCompliance.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:dpsfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeSystemFileMIB':dlinkPrimeSystemFileMIB,'dpsfMIBNotifications':dpsfMIBNotifications,'dpsfMIBObjects':dpsfMIBObjects,'dpsfBootInfoObjects':dpsfBootInfoObjects,_M:dpsfCheckingBootImageCheck,_N:dpsfBootImageCheckResult,'dpsfBootImageTable':dpsfBootImageTable,'dpsfBootImageEntry':dpsfBootImageEntry,_J:dpsfBootImageIndex,_O:dpsfBootImageInWorking,'dpsfCopyTable':dpsfCopyTable,'dpsfCopyEntry':dpsfCopyEntry,_K:dpsfCopyIndex,_P:dpsfCopyType,_Q:dpsfCopySrcUrl,_R:dpsfCopyDstUrl,_S:dpsfCopyRemoteAddr,_T:dpsfCopyErrorStatus,_U:dpsfCopyRowStatus,'dpsfCfgReplaceTable':dpsfCfgReplaceTable,'dpsfCfgReplaceEntry':dpsfCfgReplaceEntry,_L:dpsfCfgReplaceIndex,_V:dpsfCfgReplaceSrcType,_W:dpsfCfgReplaceSrcUrl,_X:dpsfCfgReplaceRemoteAddr,_Y:dpsfCfgReplaceErrorStatus,_Z:dpsfCfgReplaceRowStatus,_a:dpsfClearRunCfg,_b:dpsfResetSystem,'dpsfMIBConformance':dpsfMIBConformance,'dpsfCompliances':dpsfCompliances,'dpsfCompliance':dpsfCompliance,'dpsfGroups':dpsfGroups,_c:dpsfBootInfoGroup,_d:dpsfCopyGroup,_e:dpsfCfgReplaceGroup,_f:dpsfClearCfgGroup})