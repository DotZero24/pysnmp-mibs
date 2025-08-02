_G='2012-02-14 00:00'
_F='read-write'
_E='read-only'
_D='ifPoeIndex'
_C='FS-POE-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fsPoeMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,110))
if mibBuilder.loadTexts:fsPoeMIB.setRevisions((_G,_G))
_FsPoeConfigMIBObjects_ObjectIdentity=ObjectIdentity
fsPoeConfigMIBObjects=_FsPoeConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,110,1))
_FsIfPoeTable_Object=MibTable
fsIfPoeTable=_FsIfPoeTable_Object((1,3,6,1,4,1,52642,1,1,10,2,110,1,1))
if mibBuilder.loadTexts:fsIfPoeTable.setStatus(_A)
_FsIfPoeEntry_Object=MibTableRow
fsIfPoeEntry=_FsIfPoeEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,110,1,1,1))
fsIfPoeEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:fsIfPoeEntry.setStatus(_A)
class _IfPoeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IfPoeIndex_Type.__name__=_B
_IfPoeIndex_Object=MibTableColumn
ifPoeIndex=_IfPoeIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,110,1,1,1,1),_IfPoeIndex_Type())
ifPoeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ifPoeIndex.setStatus(_A)
_IfIsPoe_Type=TruthValue
_IfIsPoe_Object=MibTableColumn
ifIsPoe=_IfIsPoe_Object((1,3,6,1,4,1,52642,1,1,10,2,110,1,1,1,2),_IfIsPoe_Type())
ifIsPoe.setMaxAccess(_E)
if mibBuilder.loadTexts:ifIsPoe.setStatus(_A)
class _IfPoeEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_IfPoeEnable_Type.__name__=_B
_IfPoeEnable_Object=MibTableColumn
ifPoeEnable=_IfPoeEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,110,1,1,1,3),_IfPoeEnable_Type())
ifPoeEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:ifPoeEnable.setStatus(_A)
class _IfPoePwrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_IfPoePwrStatus_Type.__name__=_B
_IfPoePwrStatus_Object=MibTableColumn
ifPoePwrStatus=_IfPoePwrStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,110,1,1,1,4),_IfPoePwrStatus_Type())
ifPoePwrStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ifPoePwrStatus.setStatus(_A)
class _IfPoeMaxPwrSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IfPoeMaxPwrSet_Type.__name__=_B
_IfPoeMaxPwrSet_Object=MibTableColumn
ifPoeMaxPwrSet=_IfPoeMaxPwrSet_Object((1,3,6,1,4,1,52642,1,1,10,2,110,1,1,1,5),_IfPoeMaxPwrSet_Type())
ifPoeMaxPwrSet.setMaxAccess(_F)
if mibBuilder.loadTexts:ifPoeMaxPwrSet.setStatus(_A)
class _IfPoePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('critical',1),('high',2),('low',3)))
_IfPoePriority_Type.__name__=_B
_IfPoePriority_Object=MibTableColumn
ifPoePriority=_IfPoePriority_Object((1,3,6,1,4,1,52642,1,1,10,2,110,1,1,1,6),_IfPoePriority_Type())
ifPoePriority.setMaxAccess(_F)
if mibBuilder.loadTexts:ifPoePriority.setStatus(_A)
_IfPoeConsumingPwr_Type=Integer32
_IfPoeConsumingPwr_Object=MibTableColumn
ifPoeConsumingPwr=_IfPoeConsumingPwr_Object((1,3,6,1,4,1,52642,1,1,10,2,110,1,1,1,7),_IfPoeConsumingPwr_Type())
ifPoeConsumingPwr.setMaxAccess(_E)
if mibBuilder.loadTexts:ifPoeConsumingPwr.setStatus(_A)
_IfIsHPoe_Type=TruthValue
_IfIsHPoe_Object=MibTableColumn
ifIsHPoe=_IfIsHPoe_Object((1,3,6,1,4,1,52642,1,1,10,2,110,1,1,1,8),_IfIsHPoe_Type())
ifIsHPoe.setMaxAccess(_E)
if mibBuilder.loadTexts:ifIsHPoe.setStatus(_A)
_FsPoeTraps_ObjectIdentity=ObjectIdentity
fsPoeTraps=_FsPoeTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,110,2))
ifPoePowerOffTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,110,2,1))
ifPoePowerOffTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ifPoePowerOffTrap.setStatus(_A)
ifPoePowerOnTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,110,2,2))
ifPoePowerOnTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ifPoePowerOnTrap.setStatus(_A)
ifPoePboxAbnormalTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,110,2,3))
ifPoePboxAbnormalTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ifPoePboxAbnormalTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsPoeMIB':fsPoeMIB,'fsPoeConfigMIBObjects':fsPoeConfigMIBObjects,'fsIfPoeTable':fsIfPoeTable,'fsIfPoeEntry':fsIfPoeEntry,_D:ifPoeIndex,'ifIsPoe':ifIsPoe,'ifPoeEnable':ifPoeEnable,'ifPoePwrStatus':ifPoePwrStatus,'ifPoeMaxPwrSet':ifPoeMaxPwrSet,'ifPoePriority':ifPoePriority,'ifPoeConsumingPwr':ifPoeConsumingPwr,'ifIsHPoe':ifIsHPoe,'fsPoeTraps':fsPoeTraps,'ifPoePowerOffTrap':ifPoePowerOffTrap,'ifPoePowerOnTrap':ifPoePowerOnTrap,'ifPoePboxAbnormalTrap':ifPoePboxAbnormalTrap})