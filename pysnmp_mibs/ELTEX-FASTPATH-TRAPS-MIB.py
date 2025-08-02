_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesFastpath,=mibBuilder.importSymbols('ELTEX-MES-FASTPATH-MIB','eltMesFastpath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltFastpathTrapsMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,103,4))
if mibBuilder.loadTexts:eltFastpathTrapsMIB.setRevisions(('2017-10-06 00:00',))
_EfpTrapsObjects_ObjectIdentity=ObjectIdentity
efpTrapsObjects=_EfpTrapsObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,103,4,1))
class _EfpGeneralTestTrapStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('success',2),('failure',3),('uninitialized',4)))
_EfpGeneralTestTrapStatus_Type.__name__=_B
_EfpGeneralTestTrapStatus_Object=MibScalar
efpGeneralTestTrapStatus=_EfpGeneralTestTrapStatus_Object((1,3,6,1,4,1,35265,1,103,4,1,1),_EfpGeneralTestTrapStatus_Type())
efpGeneralTestTrapStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:efpGeneralTestTrapStatus.setStatus(_A)
_EfpTrapsNotifications_ObjectIdentity=ObjectIdentity
efpTrapsNotifications=_EfpTrapsNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,103,4,2))
_EfpTrapsNotificationsPrefix_ObjectIdentity=ObjectIdentity
efpTrapsNotificationsPrefix=_EfpTrapsNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,103,4,2,0))
_EfpTrapsConformance_ObjectIdentity=ObjectIdentity
efpTrapsConformance=_EfpTrapsConformance_ObjectIdentity((1,3,6,1,4,1,35265,1,103,4,3))
efpWriteMemoryTrap=NotificationType((1,3,6,1,4,1,35265,1,103,4,2,0,1))
if mibBuilder.loadTexts:efpWriteMemoryTrap.setStatus(_A)
efpCopyFinishedTrap=NotificationType((1,3,6,1,4,1,35265,1,103,4,2,0,2))
if mibBuilder.loadTexts:efpCopyFinishedTrap.setStatus(_A)
efpCopyFailedTrap=NotificationType((1,3,6,1,4,1,35265,1,103,4,2,0,3))
if mibBuilder.loadTexts:efpCopyFailedTrap.setStatus(_A)
efpGeneralTestTrap=NotificationType((1,3,6,1,4,1,35265,1,103,4,2,0,4))
if mibBuilder.loadTexts:efpGeneralTestTrap.setStatus(_A)
efpConfigurationReloadedTrap=NotificationType((1,3,6,1,4,1,35265,1,103,4,2,0,5))
if mibBuilder.loadTexts:efpConfigurationReloadedTrap.setStatus(_A)
efpConfigurationReloadFailedTrap=NotificationType((1,3,6,1,4,1,35265,1,103,4,2,0,6))
if mibBuilder.loadTexts:efpConfigurationReloadFailedTrap.setStatus(_A)
mibBuilder.exportSymbols('ELTEX-FASTPATH-TRAPS-MIB',**{'eltFastpathTrapsMIB':eltFastpathTrapsMIB,'efpTrapsObjects':efpTrapsObjects,'efpGeneralTestTrapStatus':efpGeneralTestTrapStatus,'efpTrapsNotifications':efpTrapsNotifications,'efpTrapsNotificationsPrefix':efpTrapsNotificationsPrefix,'efpWriteMemoryTrap':efpWriteMemoryTrap,'efpCopyFinishedTrap':efpCopyFinishedTrap,'efpCopyFailedTrap':efpCopyFailedTrap,'efpGeneralTestTrap':efpGeneralTestTrap,'efpConfigurationReloadedTrap':efpConfigurationReloadedTrap,'efpConfigurationReloadFailedTrap':efpConfigurationReloadFailedTrap,'efpTrapsConformance':efpTrapsConformance})