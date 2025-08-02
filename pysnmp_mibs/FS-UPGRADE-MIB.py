_J='read-write'
_I='DisplayString'
_H='Integer32'
_G='fsSystemUpgradeFailVersion'
_F='fsSystemUpgradeFailReason'
_E='fsSystemUpgradeFailNo'
_D='fsSystemCurrtenVersion'
_C='read-only'
_B='current'
_A='FS-UPGRADE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('FS-TC','ConfigStatus','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsUpgradeMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,158))
if mibBuilder.loadTexts:fsUpgradeMIB.setRevisions(('2018-01-02 00:00',))
_FsUpgradeMIBObjects_ObjectIdentity=ObjectIdentity
fsUpgradeMIBObjects=_FsUpgradeMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,158,1))
_FsUpgradeMIBGroups_ObjectIdentity=ObjectIdentity
fsUpgradeMIBGroups=_FsUpgradeMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,158,1,1))
class _FsFileSystemUpgradeDownloadUrl_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsFileSystemUpgradeDownloadUrl_Type.__name__=_I
_FsFileSystemUpgradeDownloadUrl_Object=MibScalar
fsFileSystemUpgradeDownloadUrl=_FsFileSystemUpgradeDownloadUrl_Object((1,3,6,1,4,1,52642,1,1,10,2,158,1,1,1),_FsFileSystemUpgradeDownloadUrl_Type())
fsFileSystemUpgradeDownloadUrl.setMaxAccess(_J)
if mibBuilder.loadTexts:fsFileSystemUpgradeDownloadUrl.setStatus(_B)
class _FsFileSystemUpgradeDownloadFlag_Type(Integer32):defaultValue=0
_FsFileSystemUpgradeDownloadFlag_Type.__name__=_H
_FsFileSystemUpgradeDownloadFlag_Object=MibScalar
fsFileSystemUpgradeDownloadFlag=_FsFileSystemUpgradeDownloadFlag_Object((1,3,6,1,4,1,52642,1,1,10,2,158,1,1,2),_FsFileSystemUpgradeDownloadFlag_Type())
fsFileSystemUpgradeDownloadFlag.setMaxAccess(_J)
if mibBuilder.loadTexts:fsFileSystemUpgradeDownloadFlag.setStatus(_B)
_FsUpgradeMIBTraps_ObjectIdentity=ObjectIdentity
fsUpgradeMIBTraps=_FsUpgradeMIBTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,158,2))
_FsUpgradeMIBConformance_ObjectIdentity=ObjectIdentity
fsUpgradeMIBConformance=_FsUpgradeMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,158,3))
_FsUpgradeMIBCompliances_ObjectIdentity=ObjectIdentity
fsUpgradeMIBCompliances=_FsUpgradeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,158,3,1))
_FsSystemCurrtenVersion_Type=DisplayString
_FsSystemCurrtenVersion_Object=MibScalar
fsSystemCurrtenVersion=_FsSystemCurrtenVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,158,3,1,1),_FsSystemCurrtenVersion_Type())
fsSystemCurrtenVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSystemCurrtenVersion.setStatus(_B)
_FsSystemUpgradeFailNo_Type=Integer32
_FsSystemUpgradeFailNo_Object=MibScalar
fsSystemUpgradeFailNo=_FsSystemUpgradeFailNo_Object((1,3,6,1,4,1,52642,1,1,10,2,158,3,1,2),_FsSystemUpgradeFailNo_Type())
fsSystemUpgradeFailNo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSystemUpgradeFailNo.setStatus(_B)
_FsSystemUpgradeFailReason_Type=DisplayString
_FsSystemUpgradeFailReason_Object=MibScalar
fsSystemUpgradeFailReason=_FsSystemUpgradeFailReason_Object((1,3,6,1,4,1,52642,1,1,10,2,158,3,1,3),_FsSystemUpgradeFailReason_Type())
fsSystemUpgradeFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSystemUpgradeFailReason.setStatus(_B)
_FsSystemUpgradeFailVersion_Type=DisplayString
_FsSystemUpgradeFailVersion_Object=MibScalar
fsSystemUpgradeFailVersion=_FsSystemUpgradeFailVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,158,3,1,4),_FsSystemUpgradeFailVersion_Type())
fsSystemUpgradeFailVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSystemUpgradeFailVersion.setStatus(_B)
fsUpgradeFailTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,158,2,1))
fsUpgradeFailTrap.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:fsUpgradeFailTrap.setStatus(_B)
fsUpgradeFailRecovTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,158,2,2))
fsUpgradeFailRecovTrap.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:fsUpgradeFailRecovTrap.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fsUpgradeMIB':fsUpgradeMIB,'fsUpgradeMIBObjects':fsUpgradeMIBObjects,'fsUpgradeMIBGroups':fsUpgradeMIBGroups,'fsFileSystemUpgradeDownloadUrl':fsFileSystemUpgradeDownloadUrl,'fsFileSystemUpgradeDownloadFlag':fsFileSystemUpgradeDownloadFlag,'fsUpgradeMIBTraps':fsUpgradeMIBTraps,'fsUpgradeFailTrap':fsUpgradeFailTrap,'fsUpgradeFailRecovTrap':fsUpgradeFailRecovTrap,'fsUpgradeMIBConformance':fsUpgradeMIBConformance,'fsUpgradeMIBCompliances':fsUpgradeMIBCompliances,_D:fsSystemCurrtenVersion,_E:fsSystemUpgradeFailNo,_F:fsSystemUpgradeFailReason,_G:fsSystemUpgradeFailVersion})