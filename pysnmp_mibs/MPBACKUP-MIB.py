_F='backupIfIndex'
_E='MPBACKUP-MIB'
_D='OctetString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mpBackupMib=ModuleIdentity((1,3,6,1,4,1,5651,3,29))
_MpBackupConf_ObjectIdentity=ObjectIdentity
mpBackupConf=_MpBackupConf_ObjectIdentity((1,3,6,1,4,1,5651,3,29,1))
_MpBackupConfTable_Object=MibTable
mpBackupConfTable=_MpBackupConfTable_Object((1,3,6,1,4,1,5651,3,29,1,1))
if mibBuilder.loadTexts:mpBackupConfTable.setStatus(_A)
_MpBackupConfEntry_Object=MibTableRow
mpBackupConfEntry=_MpBackupConfEntry_Object((1,3,6,1,4,1,5651,3,29,1,1,1))
mpBackupConfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mpBackupConfEntry.setStatus(_A)
_BackupIfIndex_Type=Integer32
_BackupIfIndex_Object=MibTableColumn
backupIfIndex=_BackupIfIndex_Object((1,3,6,1,4,1,5651,3,29,1,1,1,1),_BackupIfIndex_Type())
backupIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:backupIfIndex.setStatus(_A)
_BackupIfName_Type=OctetString
_BackupIfName_Object=MibTableColumn
backupIfName=_BackupIfName_Object((1,3,6,1,4,1,5651,3,29,1,1,1,2),_BackupIfName_Type())
backupIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:backupIfName.setStatus(_A)
class _BackupFlag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_BackupFlag_Type.__name__=_D
_BackupFlag_Object=MibTableColumn
backupFlag=_BackupFlag_Object((1,3,6,1,4,1,5651,3,29,1,1,1,3),_BackupFlag_Type())
backupFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:backupFlag.setStatus(_A)
_BackupDelayAct_Type=Unsigned32
_BackupDelayAct_Object=MibTableColumn
backupDelayAct=_BackupDelayAct_Object((1,3,6,1,4,1,5651,3,29,1,1,1,4),_BackupDelayAct_Type())
backupDelayAct.setMaxAccess(_B)
if mibBuilder.loadTexts:backupDelayAct.setStatus(_A)
_BackupDelayDeact_Type=Unsigned32
_BackupDelayDeact_Object=MibTableColumn
backupDelayDeact=_BackupDelayDeact_Object((1,3,6,1,4,1,5651,3,29,1,1,1,5),_BackupDelayDeact_Type())
backupDelayDeact.setMaxAccess(_B)
if mibBuilder.loadTexts:backupDelayDeact.setStatus(_A)
class _BackupLoadAct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BackupLoadAct_Type.__name__=_C
_BackupLoadAct_Object=MibTableColumn
backupLoadAct=_BackupLoadAct_Object((1,3,6,1,4,1,5651,3,29,1,1,1,6),_BackupLoadAct_Type())
backupLoadAct.setMaxAccess(_B)
if mibBuilder.loadTexts:backupLoadAct.setStatus(_A)
class _BackupLoadDeact_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BackupLoadDeact_Type.__name__=_C
_BackupLoadDeact_Object=MibTableColumn
backupLoadDeact=_BackupLoadDeact_Object((1,3,6,1,4,1,5651,3,29,1,1,1,7),_BackupLoadDeact_Type())
backupLoadDeact.setMaxAccess(_B)
if mibBuilder.loadTexts:backupLoadDeact.setStatus(_A)
_BackupRowStatus_Type=RowStatus
_BackupRowStatus_Object=MibTableColumn
backupRowStatus=_BackupRowStatus_Object((1,3,6,1,4,1,5651,3,29,1,1,1,8),_BackupRowStatus_Type())
backupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:backupRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mpBackupMib':mpBackupMib,'mpBackupConf':mpBackupConf,'mpBackupConfTable':mpBackupConfTable,'mpBackupConfEntry':mpBackupConfEntry,_F:backupIfIndex,'backupIfName':backupIfName,'backupFlag':backupFlag,'backupDelayAct':backupDelayAct,'backupDelayDeact':backupDelayDeact,'backupLoadAct':backupLoadAct,'backupLoadDeact':backupLoadDeact,'backupRowStatus':backupRowStatus})