_J='aluBootLoaderNotificationGroup'
_I='aluBootLoaderGroup'
_H='aluBootLoaderUpdateResult'
_G='aluBootLoaderUpdateFile'
_F='aluBootLoaderForceUpdateFile'
_E='read-write'
_D='aluBootLoaderUpdateResultMessage'
_C='DisplayString'
_B='current'
_A='ALU-BOOT-LOADER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aluCardObjs,aluChassisNotification=mibBuilder.importSymbols('ALU-CHASSIS-MIB','aluCardObjs','aluChassisNotification')
aluSARConfs,aluSARMIBModules=mibBuilder.importSymbols('ALU-SAR-GLOBAL-MIB','aluSARConfs','aluSARMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
aluBootLoaderMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,1,1,1,3,17))
if mibBuilder.loadTexts:aluBootLoaderMIBModule.setRevisions(('1914-06-02 00:00',))
_AluBootLoaderMIBConformance_ObjectIdentity=ObjectIdentity
aluBootLoaderMIBConformance=_AluBootLoaderMIBConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,27))
_AluBootLoaderMIBCompliances_ObjectIdentity=ObjectIdentity
aluBootLoaderMIBCompliances=_AluBootLoaderMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,27,1))
_AluBootLoaderMIBGroups_ObjectIdentity=ObjectIdentity
aluBootLoaderMIBGroups=_AluBootLoaderMIBGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,27,2))
class _AluBootLoaderUpdateFile_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,180))
_AluBootLoaderUpdateFile_Type.__name__=_C
_AluBootLoaderUpdateFile_Object=MibScalar
aluBootLoaderUpdateFile=_AluBootLoaderUpdateFile_Object((1,3,6,1,4,1,6527,6,1,2,2,2,3,1),_AluBootLoaderUpdateFile_Type())
aluBootLoaderUpdateFile.setMaxAccess(_E)
if mibBuilder.loadTexts:aluBootLoaderUpdateFile.setStatus(_B)
class _AluBootLoaderForceUpdateFile_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,180))
_AluBootLoaderForceUpdateFile_Type.__name__=_C
_AluBootLoaderForceUpdateFile_Object=MibScalar
aluBootLoaderForceUpdateFile=_AluBootLoaderForceUpdateFile_Object((1,3,6,1,4,1,6527,6,1,2,2,2,3,2),_AluBootLoaderForceUpdateFile_Type())
aluBootLoaderForceUpdateFile.setMaxAccess(_E)
if mibBuilder.loadTexts:aluBootLoaderForceUpdateFile.setStatus(_B)
class _AluBootLoaderUpdateResultMessage_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,180))
_AluBootLoaderUpdateResultMessage_Type.__name__=_C
_AluBootLoaderUpdateResultMessage_Object=MibScalar
aluBootLoaderUpdateResultMessage=_AluBootLoaderUpdateResultMessage_Object((1,3,6,1,4,1,6527,6,1,2,2,2,3,3),_AluBootLoaderUpdateResultMessage_Type())
aluBootLoaderUpdateResultMessage.setMaxAccess('read-only')
if mibBuilder.loadTexts:aluBootLoaderUpdateResultMessage.setStatus(_B)
aluBootLoaderGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,27,2,1))
aluBootLoaderGroup.setObjects(*((_A,_F),(_A,_G),(_A,_D)))
if mibBuilder.loadTexts:aluBootLoaderGroup.setStatus(_B)
aluBootLoaderUpdateResult=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,2,1,0,18))
aluBootLoaderUpdateResult.setObjects((_A,_D))
if mibBuilder.loadTexts:aluBootLoaderUpdateResult.setStatus(_B)
aluBootLoaderNotificationGroup=NotificationGroup((1,3,6,1,4,1,6527,6,1,2,1,27,2,2))
aluBootLoaderNotificationGroup.setObjects((_A,_H))
if mibBuilder.loadTexts:aluBootLoaderNotificationGroup.setStatus(_B)
aluBootLoader7705V6v2Compliance=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,27,1,1))
aluBootLoader7705V6v2Compliance.setObjects(*((_A,_I),(_A,_J)))
if mibBuilder.loadTexts:aluBootLoader7705V6v2Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'aluBootLoaderMIBModule':aluBootLoaderMIBModule,'aluBootLoaderMIBConformance':aluBootLoaderMIBConformance,'aluBootLoaderMIBCompliances':aluBootLoaderMIBCompliances,'aluBootLoader7705V6v2Compliance':aluBootLoader7705V6v2Compliance,'aluBootLoaderMIBGroups':aluBootLoaderMIBGroups,_I:aluBootLoaderGroup,_J:aluBootLoaderNotificationGroup,_G:aluBootLoaderUpdateFile,_F:aluBootLoaderForceUpdateFile,_D:aluBootLoaderUpdateResultMessage,_H:aluBootLoaderUpdateResult})