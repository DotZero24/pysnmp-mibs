_G='mpFileCommand'
_F='MPFILE-MIB'
_E='OctetString'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
mpFileMib=ModuleIdentity((1,3,6,1,4,1,5651,3,3))
class _MpSoftVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_MpSoftVersion_Type.__name__=_D
_MpSoftVersion_Object=MibScalar
mpSoftVersion=_MpSoftVersion_Object((1,3,6,1,4,1,5651,3,3,1),_MpSoftVersion_Type())
mpSoftVersion.setMaxAccess('read-only')
if mibBuilder.loadTexts:mpSoftVersion.setStatus(_A)
_MpFileTable_Object=MibTable
mpFileTable=_MpFileTable_Object((1,3,6,1,4,1,5651,3,3,2))
if mibBuilder.loadTexts:mpFileTable.setStatus(_A)
_MpFileEntry_Object=MibTableRow
mpFileEntry=_MpFileEntry_Object((1,3,6,1,4,1,5651,3,3,2,1))
mpFileEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:mpFileEntry.setStatus(_A)
class _MpFileCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('backup',1),('restore',2),('update',3),('reboot',4)))
_MpFileCommand_Type.__name__=_C
_MpFileCommand_Object=MibTableColumn
mpFileCommand=_MpFileCommand_Object((1,3,6,1,4,1,5651,3,3,2,1,1),_MpFileCommand_Type())
mpFileCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:mpFileCommand.setStatus(_A)
class _MpFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_MpFileName_Type.__name__=_D
_MpFileName_Object=MibTableColumn
mpFileName=_MpFileName_Object((1,3,6,1,4,1,5651,3,3,2,1,2),_MpFileName_Type())
mpFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpFileName.setStatus(_A)
_MpFileSize_Type=Integer32
_MpFileSize_Object=MibTableColumn
mpFileSize=_MpFileSize_Object((1,3,6,1,4,1,5651,3,3,2,1,3),_MpFileSize_Type())
mpFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpFileSize.setStatus(_A)
class _MpFileConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('running',2),('startup',3)))
_MpFileConfigType_Type.__name__=_C
_MpFileConfigType_Object=MibTableColumn
mpFileConfigType=_MpFileConfigType_Object((1,3,6,1,4,1,5651,3,3,2,1,4),_MpFileConfigType_Type())
mpFileConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpFileConfigType.setStatus(_A)
class _MpFileTransMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ftp',1),('tftp',2),('rcp',3)))
_MpFileTransMode_Type.__name__=_C
_MpFileTransMode_Object=MibTableColumn
mpFileTransMode=_MpFileTransMode_Object((1,3,6,1,4,1,5651,3,3,2,1,5),_MpFileTransMode_Type())
mpFileTransMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mpFileTransMode.setStatus(_A)
_MpFileServerIP_Type=IpAddress
_MpFileServerIP_Object=MibTableColumn
mpFileServerIP=_MpFileServerIP_Object((1,3,6,1,4,1,5651,3,3,2,1,6),_MpFileServerIP_Type())
mpFileServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:mpFileServerIP.setStatus(_A)
class _MpFileUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_MpFileUser_Type.__name__=_D
_MpFileUser_Object=MibTableColumn
mpFileUser=_MpFileUser_Object((1,3,6,1,4,1,5651,3,3,2,1,7),_MpFileUser_Type())
mpFileUser.setMaxAccess(_B)
if mibBuilder.loadTexts:mpFileUser.setStatus(_A)
class _MpFilePassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpFilePassword_Type.__name__=_E
_MpFilePassword_Object=MibTableColumn
mpFilePassword=_MpFilePassword_Object((1,3,6,1,4,1,5651,3,3,2,1,8),_MpFilePassword_Type())
mpFilePassword.setMaxAccess(_B)
if mibBuilder.loadTexts:mpFilePassword.setStatus(_A)
class _MpFileEncrypt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('none',1))
_MpFileEncrypt_Type.__name__=_C
_MpFileEncrypt_Object=MibTableColumn
mpFileEncrypt=_MpFileEncrypt_Object((1,3,6,1,4,1,5651,3,3,2,1,9),_MpFileEncrypt_Type())
mpFileEncrypt.setMaxAccess(_B)
if mibBuilder.loadTexts:mpFileEncrypt.setStatus(_A)
_MpRtrCommand_ObjectIdentity=ObjectIdentity
mpRtrCommand=_MpRtrCommand_ObjectIdentity((1,3,6,1,4,1,5651,3,3,3))
class _MpRtrCommWrite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noop',1),('write',2)))
_MpRtrCommWrite_Type.__name__=_C
_MpRtrCommWrite_Object=MibScalar
mpRtrCommWrite=_MpRtrCommWrite_Object((1,3,6,1,4,1,5651,3,3,3,1),_MpRtrCommWrite_Type())
mpRtrCommWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:mpRtrCommWrite.setStatus(_A)
class _MpRtrCommBackup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MpRtrCommBackup_Type.__name__=_C
_MpRtrCommBackup_Object=MibScalar
mpRtrCommBackup=_MpRtrCommBackup_Object((1,3,6,1,4,1,5651,3,3,3,2),_MpRtrCommBackup_Type())
mpRtrCommBackup.setMaxAccess(_B)
if mibBuilder.loadTexts:mpRtrCommBackup.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'mpFileMib':mpFileMib,'mpSoftVersion':mpSoftVersion,'mpFileTable':mpFileTable,'mpFileEntry':mpFileEntry,_G:mpFileCommand,'mpFileName':mpFileName,'mpFileSize':mpFileSize,'mpFileConfigType':mpFileConfigType,'mpFileTransMode':mpFileTransMode,'mpFileServerIP':mpFileServerIP,'mpFileUser':mpFileUser,'mpFilePassword':mpFilePassword,'mpFileEncrypt':mpFileEncrypt,'mpRtrCommand':mpRtrCommand,'mpRtrCommWrite':mpRtrCommWrite,'mpRtrCommBackup':mpRtrCommBackup})