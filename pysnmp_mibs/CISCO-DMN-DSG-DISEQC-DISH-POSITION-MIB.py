_M='installer'
_L='gotoSatellite'
_K='notApplicable'
_J='fineAdjustmentWest'
_I='coarseAdjustmentEast'
_H='writeOnly'
_G='diSEqCInstance'
_F='CISCO-DMN-DSG-DISEQC-DISH-POSITION-MIB'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
ciscoDSGDiSEqC=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,19))
if mibBuilder.loadTexts:ciscoDSGDiSEqC.setRevisions(('2010-08-30 11:00','2010-03-22 05:00','2010-02-12 12:00','2009-12-07 12:00'))
_DiSEqCTable_Object=MibTable
diSEqCTable=_DiSEqCTable_Object((1,3,6,1,4,1,1429,2,2,5,19,1))
if mibBuilder.loadTexts:diSEqCTable.setStatus(_A)
_DiSEqCEntry_Object=MibTableRow
diSEqCEntry=_DiSEqCEntry_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1))
diSEqCEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:diSEqCEntry.setStatus(_A)
class _DiSEqCInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_DiSEqCInstance_Type.__name__=_B
_DiSEqCInstance_Object=MibTableColumn
diSEqCInstance=_DiSEqCInstance_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,1),_DiSEqCInstance_Type())
diSEqCInstance.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:diSEqCInstance.setStatus(_A)
class _DiSEqCEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_DiSEqCEnable_Type.__name__=_B
_DiSEqCEnable_Object=MibTableColumn
diSEqCEnable=_DiSEqCEnable_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,2),_DiSEqCEnable_Type())
diSEqCEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:diSEqCEnable.setStatus(_A)
class _DiSEqCDishPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,750))
_DiSEqCDishPosition_Type.__name__=_B
_DiSEqCDishPosition_Object=MibTableColumn
diSEqCDishPosition=_DiSEqCDishPosition_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,3),_DiSEqCDishPosition_Type())
diSEqCDishPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:diSEqCDishPosition.setStatus(_A)
class _DiSEqCPositionJog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_I,2),('coarseAdjustmentWest',3),('fineAdjustmentEast',4),(_J,5)))
_DiSEqCPositionJog_Type.__name__=_B
_DiSEqCPositionJog_Object=MibTableColumn
diSEqCPositionJog=_DiSEqCPositionJog_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,4),_DiSEqCPositionJog_Type())
diSEqCPositionJog.setMaxAccess(_C)
if mibBuilder.loadTexts:diSEqCPositionJog.setStatus(_A)
class _DiSEqCEWFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('east',1),('west',2),(_K,3)))
_DiSEqCEWFlag_Type.__name__=_B
_DiSEqCEWFlag_Object=MibTableColumn
diSEqCEWFlag=_DiSEqCEWFlag_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,5),_DiSEqCEWFlag_Type())
diSEqCEWFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:diSEqCEWFlag.setStatus(_A)
class _DiSEqCSatSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DiSEqCSatSelect_Type.__name__=_B
_DiSEqCSatSelect_Object=MibTableColumn
diSEqCSatSelect=_DiSEqCSatSelect_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,6),_DiSEqCSatSelect_Type())
diSEqCSatSelect.setMaxAccess(_C)
if mibBuilder.loadTexts:diSEqCSatSelect.setStatus(_A)
class _DiSEqCInstallerAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('none',1),('continuousWestMovement',2),('continuousEastMovement',3),('stopMove',4),('gotoAbsolutePositionWest',5),('gotoAbsolutePositionEast',6),('gotoReference',7),(_L,8),('storeSatellite',9),('clearLimits',10),('storeEastLimits',11),('storeWestLimits',12),('calculatePosition',13)))
_DiSEqCInstallerAction_Type.__name__=_B
_DiSEqCInstallerAction_Object=MibTableColumn
diSEqCInstallerAction=_DiSEqCInstallerAction_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,7),_DiSEqCInstallerAction_Type())
diSEqCInstallerAction.setMaxAccess(_C)
if mibBuilder.loadTexts:diSEqCInstallerAction.setStatus(_A)
class _DiSEqCUserAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),(_L,2)))
_DiSEqCUserAction_Type.__name__=_B
_DiSEqCUserAction_Object=MibTableColumn
diSEqCUserAction=_DiSEqCUserAction_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,8),_DiSEqCUserAction_Type())
diSEqCUserAction.setMaxAccess(_C)
if mibBuilder.loadTexts:diSEqCUserAction.setStatus(_A)
class _DiSEqCMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('user',2)))
_DiSEqCMode_Type.__name__=_B
_DiSEqCMode_Object=MibTableColumn
diSEqCMode=_DiSEqCMode_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,9),_DiSEqCMode_Type())
diSEqCMode.setMaxAccess(_C)
if mibBuilder.loadTexts:diSEqCMode.setStatus(_A)
class _DiSEqCAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('activate',2)))
_DiSEqCAction_Type.__name__=_B
_DiSEqCAction_Object=MibTableColumn
diSEqCAction=_DiSEqCAction_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,10),_DiSEqCAction_Type())
diSEqCAction.setMaxAccess(_C)
if mibBuilder.loadTexts:diSEqCAction.setStatus(_A)
class _DiSEqCStatusMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('user',2)))
_DiSEqCStatusMode_Type.__name__=_B
_DiSEqCStatusMode_Object=MibTableColumn
diSEqCStatusMode=_DiSEqCStatusMode_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,11),_DiSEqCStatusMode_Type())
diSEqCStatusMode.setMaxAccess(_D)
if mibBuilder.loadTexts:diSEqCStatusMode.setStatus(_A)
class _DiSEqCStatusDishPosition_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DiSEqCStatusDishPosition_Type.__name__=_E
_DiSEqCStatusDishPosition_Object=MibTableColumn
diSEqCStatusDishPosition=_DiSEqCStatusDishPosition_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,12),_DiSEqCStatusDishPosition_Type())
diSEqCStatusDishPosition.setMaxAccess(_D)
if mibBuilder.loadTexts:diSEqCStatusDishPosition.setStatus(_A)
class _DiSEqCStatusEastWestFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('east',1),('west',2),(_K,3)))
_DiSEqCStatusEastWestFlag_Type.__name__=_B
_DiSEqCStatusEastWestFlag_Object=MibTableColumn
diSEqCStatusEastWestFlag=_DiSEqCStatusEastWestFlag_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,13),_DiSEqCStatusEastWestFlag_Type())
diSEqCStatusEastWestFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:diSEqCStatusEastWestFlag.setStatus(_A)
class _DiSEqCStatusLastAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('clear',1),(_I,2),('coarseAdjustmenWest',3),('fineAdjustmenEast',4),(_J,5),('installerAction',6),('userAction',7)))
_DiSEqCStatusLastAction_Type.__name__=_B
_DiSEqCStatusLastAction_Object=MibTableColumn
diSEqCStatusLastAction=_DiSEqCStatusLastAction_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,14),_DiSEqCStatusLastAction_Type())
diSEqCStatusLastAction.setMaxAccess(_D)
if mibBuilder.loadTexts:diSEqCStatusLastAction.setStatus(_A)
class _DiSEqCStatusEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_DiSEqCStatusEnable_Type.__name__=_B
_DiSEqCStatusEnable_Object=MibTableColumn
diSEqCStatusEnable=_DiSEqCStatusEnable_Object((1,3,6,1,4,1,1429,2,2,5,19,1,1,15),_DiSEqCStatusEnable_Type())
diSEqCStatusEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:diSEqCStatusEnable.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ciscoDSGDiSEqC':ciscoDSGDiSEqC,'diSEqCTable':diSEqCTable,'diSEqCEntry':diSEqCEntry,_G:diSEqCInstance,'diSEqCEnable':diSEqCEnable,'diSEqCDishPosition':diSEqCDishPosition,'diSEqCPositionJog':diSEqCPositionJog,'diSEqCEWFlag':diSEqCEWFlag,'diSEqCSatSelect':diSEqCSatSelect,'diSEqCInstallerAction':diSEqCInstallerAction,'diSEqCUserAction':diSEqCUserAction,'diSEqCMode':diSEqCMode,'diSEqCAction':diSEqCAction,'diSEqCStatusMode':diSEqCStatusMode,'diSEqCStatusDishPosition':diSEqCStatusDishPosition,'diSEqCStatusEastWestFlag':diSEqCStatusEastWestFlag,'diSEqCStatusLastAction':diSEqCStatusLastAction,'diSEqCStatusEnable':diSEqCStatusEnable})