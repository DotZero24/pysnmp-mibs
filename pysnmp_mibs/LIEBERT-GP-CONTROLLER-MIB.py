_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lgpController,liebertControllerModuleReg=mibBuilder.importSymbols('LIEBERT-GP-REGISTRATION-MIB','lgpController','liebertControllerModuleReg')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
liebertControllerModule=ModuleIdentity((1,3,6,1,4,1,476,1,42,1,7,1))
if mibBuilder.loadTexts:liebertControllerModule.setRevisions(('2008-07-02 00:00','2008-01-10 00:00','2006-02-22 00:00'))
_LgpCtrlNumberInstalledControlModules_Type=Integer32
_LgpCtrlNumberInstalledControlModules_Object=MibScalar
lgpCtrlNumberInstalledControlModules=_LgpCtrlNumberInstalledControlModules_Object((1,3,6,1,4,1,476,1,42,3,6,1),_LgpCtrlNumberInstalledControlModules_Type())
lgpCtrlNumberInstalledControlModules.setMaxAccess(_A)
if mibBuilder.loadTexts:lgpCtrlNumberInstalledControlModules.setStatus(_B)
_LgpCtrlNumberFailedControlModules_Type=Integer32
_LgpCtrlNumberFailedControlModules_Object=MibScalar
lgpCtrlNumberFailedControlModules=_LgpCtrlNumberFailedControlModules_Object((1,3,6,1,4,1,476,1,42,3,6,2),_LgpCtrlNumberFailedControlModules_Type())
lgpCtrlNumberFailedControlModules.setMaxAccess(_A)
if mibBuilder.loadTexts:lgpCtrlNumberFailedControlModules.setStatus(_B)
_LgpCtrlNumberRedundantControlModules_Type=Integer32
_LgpCtrlNumberRedundantControlModules_Object=MibScalar
lgpCtrlNumberRedundantControlModules=_LgpCtrlNumberRedundantControlModules_Object((1,3,6,1,4,1,476,1,42,3,6,3),_LgpCtrlNumberRedundantControlModules_Type())
lgpCtrlNumberRedundantControlModules.setMaxAccess(_A)
if mibBuilder.loadTexts:lgpCtrlNumberRedundantControlModules.setStatus(_B)
_LgpCtrlNumberControlModuleWarnings_Type=Integer32
_LgpCtrlNumberControlModuleWarnings_Object=MibScalar
lgpCtrlNumberControlModuleWarnings=_LgpCtrlNumberControlModuleWarnings_Object((1,3,6,1,4,1,476,1,42,3,6,5),_LgpCtrlNumberControlModuleWarnings_Type())
lgpCtrlNumberControlModuleWarnings.setMaxAccess(_A)
if mibBuilder.loadTexts:lgpCtrlNumberControlModuleWarnings.setStatus(_B)
_LgpCtrlBoardBatteryVoltage_Type=Unsigned32
_LgpCtrlBoardBatteryVoltage_Object=MibScalar
lgpCtrlBoardBatteryVoltage=_LgpCtrlBoardBatteryVoltage_Object((1,3,6,1,4,1,476,1,42,3,6,6),_LgpCtrlBoardBatteryVoltage_Type())
lgpCtrlBoardBatteryVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:lgpCtrlBoardBatteryVoltage.setStatus(_B)
if mibBuilder.loadTexts:lgpCtrlBoardBatteryVoltage.setUnits('.01 Volts')
mibBuilder.exportSymbols('LIEBERT-GP-CONTROLLER-MIB',**{'liebertControllerModule':liebertControllerModule,'lgpCtrlNumberInstalledControlModules':lgpCtrlNumberInstalledControlModules,'lgpCtrlNumberFailedControlModules':lgpCtrlNumberFailedControlModules,'lgpCtrlNumberRedundantControlModules':lgpCtrlNumberRedundantControlModules,'lgpCtrlNumberControlModuleWarnings':lgpCtrlNumberControlModuleWarnings,'lgpCtrlBoardBatteryVoltage':lgpCtrlBoardBatteryVoltage})