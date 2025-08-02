_L='pmFTPStatus'
_K='SIAE-PMFTP-MIB'
_J='read-only'
_I='DisplayString'
_H='accessControlLoginIpAddress'
_G='SIAE-USER-MIB'
_F='equipIpSnmpAgentAddress'
_E='SIAE-EQUIP-MIB'
_D='OwnerString'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
OwnerString,=mibBuilder.importSymbols('RMON-MIB',_D)
alarmTrap,=mibBuilder.importSymbols('SIAE-ALARM-MIB','alarmTrap')
equipIpSnmpAgentAddress,=mibBuilder.importSymbols(_E,_F)
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
accessControlLoginIpAddress,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
pmFTP=ModuleIdentity((1,3,6,1,4,1,3373,1103,31))
if mibBuilder.loadTexts:pmFTP.setRevisions(('2015-03-23 00:00','2014-09-29 00:00','2014-02-03 00:00','2013-04-16 00:00'))
class _PmFTPMibVersion_Type(Integer32):defaultValue=1
_PmFTPMibVersion_Type.__name__=_B
_PmFTPMibVersion_Object=MibScalar
pmFTPMibVersion=_PmFTPMibVersion_Object((1,3,6,1,4,1,3373,1103,31,1),_PmFTPMibVersion_Type())
pmFTPMibVersion.setMaxAccess(_J)
if mibBuilder.loadTexts:pmFTPMibVersion.setStatus(_A)
class _PmFTPfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PmFTPfileName_Type.__name__=_I
_PmFTPfileName_Object=MibScalar
pmFTPfileName=_PmFTPfileName_Object((1,3,6,1,4,1,3373,1103,31,2),_PmFTPfileName_Type())
pmFTPfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:pmFTPfileName.setStatus(_A)
_PmFTPTpClass_Type=ObjectIdentifier
_PmFTPTpClass_Object=MibScalar
pmFTPTpClass=_PmFTPTpClass_Object((1,3,6,1,4,1,3373,1103,31,3),_PmFTPTpClass_Type())
pmFTPTpClass.setMaxAccess(_C)
if mibBuilder.loadTexts:pmFTPTpClass.setStatus(_A)
class _PmFTPTpRmonOwner_Type(OwnerString):defaultValue=OctetString('')
_PmFTPTpRmonOwner_Type.__name__=_D
_PmFTPTpRmonOwner_Object=MibScalar
pmFTPTpRmonOwner=_PmFTPTpRmonOwner_Object((1,3,6,1,4,1,3373,1103,31,4),_PmFTPTpRmonOwner_Type())
pmFTPTpRmonOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:pmFTPTpRmonOwner.setStatus(_A)
class _PmFTPActionRequest_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,5,6,7)));namedValues=NamedValues(*(('none',0),('dayBeforeRead',1),('currentDayRead',3),('readAll',5),('readAbort',6),('readInterval',7)))
_PmFTPActionRequest_Type.__name__=_B
_PmFTPActionRequest_Object=MibScalar
pmFTPActionRequest=_PmFTPActionRequest_Object((1,3,6,1,4,1,3373,1103,31,5),_PmFTPActionRequest_Type())
pmFTPActionRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:pmFTPActionRequest.setStatus(_A)
class _PmFTPStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('transferring',1),('completed',2),('interrupted',3),('empty',4),('deleting',5)))
_PmFTPStatus_Type.__name__=_B
_PmFTPStatus_Object=MibScalar
pmFTPStatus=_PmFTPStatus_Object((1,3,6,1,4,1,3373,1103,31,6),_PmFTPStatus_Type())
pmFTPStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:pmFTPStatus.setStatus(_A)
class _PmFTPStatusTrapNotification_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trapDisable',1),('trapEnable',2)))
_PmFTPStatusTrapNotification_Type.__name__=_B
_PmFTPStatusTrapNotification_Object=MibScalar
pmFTPStatusTrapNotification=_PmFTPStatusTrapNotification_Object((1,3,6,1,4,1,3373,1103,31,7),_PmFTPStatusTrapNotification_Type())
pmFTPStatusTrapNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:pmFTPStatusTrapNotification.setStatus(_A)
class _PmFTPCompressedFile_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_PmFTPCompressedFile_Type.__name__=_B
_PmFTPCompressedFile_Object=MibScalar
pmFTPCompressedFile=_PmFTPCompressedFile_Object((1,3,6,1,4,1,3373,1103,31,8),_PmFTPCompressedFile_Type())
pmFTPCompressedFile.setMaxAccess(_C)
if mibBuilder.loadTexts:pmFTPCompressedFile.setStatus(_A)
class _PmFTPBeginInterval_Type(Integer32):defaultValue=0
_PmFTPBeginInterval_Type.__name__=_B
_PmFTPBeginInterval_Object=MibScalar
pmFTPBeginInterval=_PmFTPBeginInterval_Object((1,3,6,1,4,1,3373,1103,31,9),_PmFTPBeginInterval_Type())
pmFTPBeginInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:pmFTPBeginInterval.setStatus(_A)
class _PmFTPEndInterval_Type(Integer32):defaultValue=0
_PmFTPEndInterval_Type.__name__=_B
_PmFTPEndInterval_Object=MibScalar
pmFTPEndInterval=_PmFTPEndInterval_Object((1,3,6,1,4,1,3373,1103,31,10),_PmFTPEndInterval_Type())
pmFTPEndInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:pmFTPEndInterval.setStatus(_A)
pmFTPStatusTrap=NotificationType((1,3,6,1,4,1,3373,1103,0,3101))
pmFTPStatusTrap.setObjects(*((_E,_F),(_K,_L),(_G,_H)))
if mibBuilder.loadTexts:pmFTPStatusTrap.setStatus(_A)
mibBuilder.exportSymbols(_K,**{'pmFTPStatusTrap':pmFTPStatusTrap,'pmFTP':pmFTP,'pmFTPMibVersion':pmFTPMibVersion,'pmFTPfileName':pmFTPfileName,'pmFTPTpClass':pmFTPTpClass,'pmFTPTpRmonOwner':pmFTPTpRmonOwner,'pmFTPActionRequest':pmFTPActionRequest,_L:pmFTPStatus,'pmFTPStatusTrapNotification':pmFTPStatusTrapNotification,'pmFTPCompressedFile':pmFTPCompressedFile,'pmFTPBeginInterval':pmFTPBeginInterval,'pmFTPEndInterval':pmFTPEndInterval})