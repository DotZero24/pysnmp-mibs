_N='zhoneRemoteSwUpgradeEnabled'
_M='zhoneRemoteSwUpgradeFileName'
_L='zhoneRemoteSwUpgradeIndexNext'
_K='zhoneRemoteSwUpgradeRowStatus'
_J='zhoneRemoteSwUpgradeSwVersion'
_I='zhoneRemoteSwUpgradeModel'
_H='zhoneRemoteSwUpgradeIndex'
_G='TruthValue'
_F='Unsigned32'
_E='Integer32'
_D='OctetString'
_C='read-write'
_B='ZHONE-REMOTE-SW-UPGRADE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G)
zhone,zhoneModules=mibBuilder.importSymbols('Zhone','zhone','zhoneModules')
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
zhoneRemoteSwUpgrade=ModuleIdentity((1,3,6,1,4,1,5504,6,117))
if mibBuilder.loadTexts:zhoneRemoteSwUpgrade.setRevisions(('2009-07-01 07:45','2009-06-09 08:33'))
_ZhoneRemoteSwUpgradeTable_Object=MibTable
zhoneRemoteSwUpgradeTable=_ZhoneRemoteSwUpgradeTable_Object((1,3,6,1,4,1,5504,6,117,1))
if mibBuilder.loadTexts:zhoneRemoteSwUpgradeTable.setStatus(_A)
_ZhoneRemoteSwUpgradeEntry_Object=MibTableRow
zhoneRemoteSwUpgradeEntry=_ZhoneRemoteSwUpgradeEntry_Object((1,3,6,1,4,1,5504,6,117,1,1))
zhoneRemoteSwUpgradeEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:zhoneRemoteSwUpgradeEntry.setStatus(_A)
class _ZhoneRemoteSwUpgradeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZhoneRemoteSwUpgradeIndex_Type.__name__=_E
_ZhoneRemoteSwUpgradeIndex_Object=MibTableColumn
zhoneRemoteSwUpgradeIndex=_ZhoneRemoteSwUpgradeIndex_Object((1,3,6,1,4,1,5504,6,117,1,1,1),_ZhoneRemoteSwUpgradeIndex_Type())
zhoneRemoteSwUpgradeIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zhoneRemoteSwUpgradeIndex.setStatus(_A)
_ZhoneRemoteSwUpgradeRowStatus_Type=ZhoneRowStatus
_ZhoneRemoteSwUpgradeRowStatus_Object=MibTableColumn
zhoneRemoteSwUpgradeRowStatus=_ZhoneRemoteSwUpgradeRowStatus_Object((1,3,6,1,4,1,5504,6,117,1,1,2),_ZhoneRemoteSwUpgradeRowStatus_Type())
zhoneRemoteSwUpgradeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneRemoteSwUpgradeRowStatus.setStatus(_A)
class _ZhoneRemoteSwUpgradeEnabled_Type(TruthValue):defaultValue=1
_ZhoneRemoteSwUpgradeEnabled_Type.__name__=_G
_ZhoneRemoteSwUpgradeEnabled_Object=MibTableColumn
zhoneRemoteSwUpgradeEnabled=_ZhoneRemoteSwUpgradeEnabled_Object((1,3,6,1,4,1,5504,6,117,1,1,3),_ZhoneRemoteSwUpgradeEnabled_Type())
zhoneRemoteSwUpgradeEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneRemoteSwUpgradeEnabled.setStatus(_A)
class _ZhoneRemoteSwUpgradeModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ZhoneRemoteSwUpgradeModel_Type.__name__=_D
_ZhoneRemoteSwUpgradeModel_Object=MibTableColumn
zhoneRemoteSwUpgradeModel=_ZhoneRemoteSwUpgradeModel_Object((1,3,6,1,4,1,5504,6,117,1,1,4),_ZhoneRemoteSwUpgradeModel_Type())
zhoneRemoteSwUpgradeModel.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneRemoteSwUpgradeModel.setStatus(_A)
class _ZhoneRemoteSwUpgradeSwVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ZhoneRemoteSwUpgradeSwVersion_Type.__name__=_D
_ZhoneRemoteSwUpgradeSwVersion_Object=MibTableColumn
zhoneRemoteSwUpgradeSwVersion=_ZhoneRemoteSwUpgradeSwVersion_Object((1,3,6,1,4,1,5504,6,117,1,1,5),_ZhoneRemoteSwUpgradeSwVersion_Type())
zhoneRemoteSwUpgradeSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneRemoteSwUpgradeSwVersion.setStatus(_A)
class _ZhoneRemoteSwUpgradeFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ZhoneRemoteSwUpgradeFileName_Type.__name__=_D
_ZhoneRemoteSwUpgradeFileName_Object=MibTableColumn
zhoneRemoteSwUpgradeFileName=_ZhoneRemoteSwUpgradeFileName_Object((1,3,6,1,4,1,5504,6,117,1,1,6),_ZhoneRemoteSwUpgradeFileName_Type())
zhoneRemoteSwUpgradeFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneRemoteSwUpgradeFileName.setStatus(_A)
class _ZhoneRemoteSwUpgradeIndexNext_Type(Unsigned32):defaultValue=1
_ZhoneRemoteSwUpgradeIndexNext_Type.__name__=_F
_ZhoneRemoteSwUpgradeIndexNext_Object=MibScalar
zhoneRemoteSwUpgradeIndexNext=_ZhoneRemoteSwUpgradeIndexNext_Object((1,3,6,1,4,1,5504,6,117,2),_ZhoneRemoteSwUpgradeIndexNext_Type())
zhoneRemoteSwUpgradeIndexNext.setMaxAccess('read-only')
if mibBuilder.loadTexts:zhoneRemoteSwUpgradeIndexNext.setStatus(_A)
_ZhoneCompliances_ObjectIdentity=ObjectIdentity
zhoneCompliances=_ZhoneCompliances_ObjectIdentity((1,3,6,1,4,1,5504,9))
_ZhoneGroups_ObjectIdentity=ObjectIdentity
zhoneGroups=_ZhoneGroups_ObjectIdentity((1,3,6,1,4,1,5504,9,1))
zhoneAutoUpgradeGroup=ObjectGroup((1,3,6,1,4,1,5504,9,1,30))
zhoneAutoUpgradeGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:zhoneAutoUpgradeGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zhoneRemoteSwUpgrade':zhoneRemoteSwUpgrade,'zhoneRemoteSwUpgradeTable':zhoneRemoteSwUpgradeTable,'zhoneRemoteSwUpgradeEntry':zhoneRemoteSwUpgradeEntry,_H:zhoneRemoteSwUpgradeIndex,_K:zhoneRemoteSwUpgradeRowStatus,_N:zhoneRemoteSwUpgradeEnabled,_I:zhoneRemoteSwUpgradeModel,_J:zhoneRemoteSwUpgradeSwVersion,_M:zhoneRemoteSwUpgradeFileName,_L:zhoneRemoteSwUpgradeIndexNext,'zhoneCompliances':zhoneCompliances,'zhoneGroups':zhoneGroups,'zhoneAutoUpgradeGroup':zhoneAutoUpgradeGroup})