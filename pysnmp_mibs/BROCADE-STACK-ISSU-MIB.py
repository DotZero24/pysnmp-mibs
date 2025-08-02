_G='brcdStackISSUStatusUnitIndex'
_F='BROCADE-STACK-ISSU-MIB'
_E='upgradeAbort'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayString,=mibBuilder.importSymbols('FOUNDRY-SN-AGENT-MIB',_D)
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','snSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
brcdStackISSUMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,41))
if mibBuilder.loadTexts:brcdStackISSUMIB.setRevisions(('2016-03-15 00:00','2017-08-07 00:00'))
_BrcdStackISSUGlobalObjects_ObjectIdentity=ObjectIdentity
brcdStackISSUGlobalObjects=_BrcdStackISSUGlobalObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,41,1))
class _BrcdStackISSUGlobalUpgradeOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',0),('primary',1),('secondary',2),('primaryOnErrorReloadPrimary',3),('primaryOnErrorReloadSecondary',4),('secondaryOnErrorReloadPrimary',5),('secondaryOnErrorReloadSecondary',6),('abort',7)))
_BrcdStackISSUGlobalUpgradeOption_Type.__name__=_C
_BrcdStackISSUGlobalUpgradeOption_Object=MibScalar
brcdStackISSUGlobalUpgradeOption=_BrcdStackISSUGlobalUpgradeOption_Object((1,3,6,1,4,1,1991,1,1,3,41,1,1),_BrcdStackISSUGlobalUpgradeOption_Type())
brcdStackISSUGlobalUpgradeOption.setMaxAccess('read-write')
if mibBuilder.loadTexts:brcdStackISSUGlobalUpgradeOption.setStatus(_A)
class _BrcdStackISSUGlobalUpgradeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('notUpgrading',0),('unitToBeUpgraded',1),('unitJoin',2),('unitVersionSync',3),('unitReady',4),('peUnitJoin',5),('peUnitVersionSync',6),('peUnitReady',7),('standbyAssignment',8),('standbySyncCompleted',9),('stackSwitchover',10),('stackSwitchoverCompleted',11),(_E,12),('waitingForReload',13)))
_BrcdStackISSUGlobalUpgradeStatus_Type.__name__=_C
_BrcdStackISSUGlobalUpgradeStatus_Object=MibScalar
brcdStackISSUGlobalUpgradeStatus=_BrcdStackISSUGlobalUpgradeStatus_Object((1,3,6,1,4,1,1991,1,1,3,41,1,2),_BrcdStackISSUGlobalUpgradeStatus_Type())
brcdStackISSUGlobalUpgradeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdStackISSUGlobalUpgradeStatus.setStatus(_A)
class _BrcdStackISSUGlobalUpgradeSystemReady_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notReadyUpgrade',0),('ready',1)))
_BrcdStackISSUGlobalUpgradeSystemReady_Type.__name__=_C
_BrcdStackISSUGlobalUpgradeSystemReady_Object=MibScalar
brcdStackISSUGlobalUpgradeSystemReady=_BrcdStackISSUGlobalUpgradeSystemReady_Object((1,3,6,1,4,1,1991,1,1,3,41,1,3),_BrcdStackISSUGlobalUpgradeSystemReady_Type())
brcdStackISSUGlobalUpgradeSystemReady.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdStackISSUGlobalUpgradeSystemReady.setStatus(_A)
_BrcdStackISSUGlobalUpgradeError_Type=DisplayString
_BrcdStackISSUGlobalUpgradeError_Object=MibScalar
brcdStackISSUGlobalUpgradeError=_BrcdStackISSUGlobalUpgradeError_Object((1,3,6,1,4,1,1991,1,1,3,41,1,4),_BrcdStackISSUGlobalUpgradeError_Type())
brcdStackISSUGlobalUpgradeError.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdStackISSUGlobalUpgradeError.setStatus(_A)
_BrcdStackISSUTableObjects_ObjectIdentity=ObjectIdentity
brcdStackISSUTableObjects=_BrcdStackISSUTableObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,41,2))
_BrcdStackISSUStatusUnitTable_Object=MibTable
brcdStackISSUStatusUnitTable=_BrcdStackISSUStatusUnitTable_Object((1,3,6,1,4,1,1991,1,1,3,41,2,1))
if mibBuilder.loadTexts:brcdStackISSUStatusUnitTable.setStatus(_A)
_BrcdStackISSUStatusUnitEntry_Object=MibTableRow
brcdStackISSUStatusUnitEntry=_BrcdStackISSUStatusUnitEntry_Object((1,3,6,1,4,1,1991,1,1,3,41,2,1,1))
brcdStackISSUStatusUnitEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:brcdStackISSUStatusUnitEntry.setStatus(_A)
_BrcdStackISSUStatusUnitIndex_Type=Integer32
_BrcdStackISSUStatusUnitIndex_Object=MibTableColumn
brcdStackISSUStatusUnitIndex=_BrcdStackISSUStatusUnitIndex_Object((1,3,6,1,4,1,1991,1,1,3,41,2,1,1,1),_BrcdStackISSUStatusUnitIndex_Type())
brcdStackISSUStatusUnitIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:brcdStackISSUStatusUnitIndex.setStatus(_A)
_BrcdStackISSUStatusUnitSequence_Type=Integer32
_BrcdStackISSUStatusUnitSequence_Object=MibTableColumn
brcdStackISSUStatusUnitSequence=_BrcdStackISSUStatusUnitSequence_Object((1,3,6,1,4,1,1991,1,1,3,41,2,1,1,2),_BrcdStackISSUStatusUnitSequence_Type())
brcdStackISSUStatusUnitSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdStackISSUStatusUnitSequence.setStatus(_A)
_BrcdStackISSUStatusUnitType_Type=DisplayString
_BrcdStackISSUStatusUnitType_Object=MibTableColumn
brcdStackISSUStatusUnitType=_BrcdStackISSUStatusUnitType_Object((1,3,6,1,4,1,1991,1,1,3,41,2,1,1,3),_BrcdStackISSUStatusUnitType_Type())
brcdStackISSUStatusUnitType.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdStackISSUStatusUnitType.setStatus(_A)
class _BrcdStackISSUStatusUnitRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('active',2),('standby',3),('member',4),('standalone',5),('spxPe',6)))
_BrcdStackISSUStatusUnitRole_Type.__name__=_C
_BrcdStackISSUStatusUnitRole_Object=MibTableColumn
brcdStackISSUStatusUnitRole=_BrcdStackISSUStatusUnitRole_Object((1,3,6,1,4,1,1991,1,1,3,41,2,1,1,4),_BrcdStackISSUStatusUnitRole_Type())
brcdStackISSUStatusUnitRole.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdStackISSUStatusUnitRole.setStatus(_A)
class _BrcdStackISSUStatusUnitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notUpgraded',0),('upgrading',1),('joined',2),('versionSyncStart',3),('versionSyncComplete',4),('upgradeComplete',5),(_E,6),('upgradePending',7)))
_BrcdStackISSUStatusUnitStatus_Type.__name__=_C
_BrcdStackISSUStatusUnitStatus_Object=MibTableColumn
brcdStackISSUStatusUnitStatus=_BrcdStackISSUStatusUnitStatus_Object((1,3,6,1,4,1,1991,1,1,3,41,2,1,1,5),_BrcdStackISSUStatusUnitStatus_Type())
brcdStackISSUStatusUnitStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdStackISSUStatusUnitStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'brcdStackISSUMIB':brcdStackISSUMIB,'brcdStackISSUGlobalObjects':brcdStackISSUGlobalObjects,'brcdStackISSUGlobalUpgradeOption':brcdStackISSUGlobalUpgradeOption,'brcdStackISSUGlobalUpgradeStatus':brcdStackISSUGlobalUpgradeStatus,'brcdStackISSUGlobalUpgradeSystemReady':brcdStackISSUGlobalUpgradeSystemReady,'brcdStackISSUGlobalUpgradeError':brcdStackISSUGlobalUpgradeError,'brcdStackISSUTableObjects':brcdStackISSUTableObjects,'brcdStackISSUStatusUnitTable':brcdStackISSUStatusUnitTable,'brcdStackISSUStatusUnitEntry':brcdStackISSUStatusUnitEntry,_G:brcdStackISSUStatusUnitIndex,'brcdStackISSUStatusUnitSequence':brcdStackISSUStatusUnitSequence,'brcdStackISSUStatusUnitType':brcdStackISSUStatusUnitType,'brcdStackISSUStatusUnitRole':brcdStackISSUStatusUnitRole,'brcdStackISSUStatusUnitStatus':brcdStackISSUStatusUnitStatus})