_I='read-create'
_H='antitheftPortIfIndex'
_G='SIAE-ANTITHEFT-MIB'
_F='DisplayString'
_E='min'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
antiTheft=ModuleIdentity((1,3,6,1,4,1,3373,1103,105))
if mibBuilder.loadTexts:antiTheft.setRevisions(('2019-03-25 00:00','2018-09-14 00:00','2018-03-15 00:00','2017-01-09 00:00'))
class _AntiTheftMibVersion_Type(Integer32):defaultValue=1
_AntiTheftMibVersion_Type.__name__=_B
_AntiTheftMibVersion_Object=MibScalar
antiTheftMibVersion=_AntiTheftMibVersion_Object((1,3,6,1,4,1,3373,1103,105,1),_AntiTheftMibVersion_Type())
antiTheftMibVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:antiTheftMibVersion.setStatus(_A)
class _AntiTheftEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AntiTheftEnable_Type.__name__=_B
_AntiTheftEnable_Object=MibScalar
antiTheftEnable=_AntiTheftEnable_Object((1,3,6,1,4,1,3373,1103,105,2),_AntiTheftEnable_Type())
antiTheftEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:antiTheftEnable.setStatus(_A)
_AntiTheftLicense_Type=OctetString
_AntiTheftLicense_Object=MibScalar
antiTheftLicense=_AntiTheftLicense_Object((1,3,6,1,4,1,3373,1103,105,3),_AntiTheftLicense_Type())
antiTheftLicense.setMaxAccess(_D)
if mibBuilder.loadTexts:antiTheftLicense.setStatus(_A)
class _AntiTheftStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unlockedUnbound',1),('unlockedBound',2),('locked',3),('notAvailable',4)))
_AntiTheftStatus_Type.__name__=_B
_AntiTheftStatus_Object=MibScalar
antiTheftStatus=_AntiTheftStatus_Object((1,3,6,1,4,1,3373,1103,105,4),_AntiTheftStatus_Type())
antiTheftStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:antiTheftStatus.setStatus(_A)
class _AntiTheftTimeout_Type(Integer32):defaultValue=4320;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,43200))
_AntiTheftTimeout_Type.__name__=_B
_AntiTheftTimeout_Object=MibScalar
antiTheftTimeout=_AntiTheftTimeout_Object((1,3,6,1,4,1,3373,1103,105,5),_AntiTheftTimeout_Type())
antiTheftTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:antiTheftTimeout.setStatus(_A)
if mibBuilder.loadTexts:antiTheftTimeout.setUnits(_E)
class _AntiTheftCountdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,43200))
_AntiTheftCountdown_Type.__name__=_B
_AntiTheftCountdown_Object=MibScalar
antiTheftCountdown=_AntiTheftCountdown_Object((1,3,6,1,4,1,3373,1103,105,6),_AntiTheftCountdown_Type())
antiTheftCountdown.setMaxAccess(_C)
if mibBuilder.loadTexts:antiTheftCountdown.setStatus(_A)
if mibBuilder.loadTexts:antiTheftCountdown.setUnits(_E)
class _AntiTheftCustomer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,7))
_AntiTheftCustomer_Type.__name__=_F
_AntiTheftCustomer_Object=MibScalar
antiTheftCustomer=_AntiTheftCustomer_Object((1,3,6,1,4,1,3373,1103,105,7),_AntiTheftCustomer_Type())
antiTheftCustomer.setMaxAccess(_C)
if mibBuilder.loadTexts:antiTheftCustomer.setStatus(_A)
_AntitheftPortMgtTable_Object=MibTable
antitheftPortMgtTable=_AntitheftPortMgtTable_Object((1,3,6,1,4,1,3373,1103,105,8))
if mibBuilder.loadTexts:antitheftPortMgtTable.setStatus(_A)
_AntitheftPortMgtEntry_Object=MibTableRow
antitheftPortMgtEntry=_AntitheftPortMgtEntry_Object((1,3,6,1,4,1,3373,1103,105,8,1))
antitheftPortMgtEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:antitheftPortMgtEntry.setStatus(_A)
_AntitheftPortIfIndex_Type=InterfaceIndex
_AntitheftPortIfIndex_Object=MibTableColumn
antitheftPortIfIndex=_AntitheftPortIfIndex_Object((1,3,6,1,4,1,3373,1103,105,8,1,1),_AntitheftPortIfIndex_Type())
antitheftPortIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:antitheftPortIfIndex.setStatus(_A)
class _AntitheftPortLock_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
_AntitheftPortLock_Type.__name__=_B
_AntitheftPortLock_Object=MibTableColumn
antitheftPortLock=_AntitheftPortLock_Object((1,3,6,1,4,1,3373,1103,105,8,1,2),_AntitheftPortLock_Type())
antitheftPortLock.setMaxAccess(_I)
if mibBuilder.loadTexts:antitheftPortLock.setStatus(_A)
_AntitheftPortRowStatus_Type=RowStatus
_AntitheftPortRowStatus_Object=MibTableColumn
antitheftPortRowStatus=_AntitheftPortRowStatus_Object((1,3,6,1,4,1,3373,1103,105,8,1,3),_AntitheftPortRowStatus_Type())
antitheftPortRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:antitheftPortRowStatus.setStatus(_A)
class _AntiTheftReconnectionTimeout_Type(Integer32):defaultValue=4320;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1440,43200))
_AntiTheftReconnectionTimeout_Type.__name__=_B
_AntiTheftReconnectionTimeout_Object=MibScalar
antiTheftReconnectionTimeout=_AntiTheftReconnectionTimeout_Object((1,3,6,1,4,1,3373,1103,105,9),_AntiTheftReconnectionTimeout_Type())
antiTheftReconnectionTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:antiTheftReconnectionTimeout.setStatus(_A)
if mibBuilder.loadTexts:antiTheftReconnectionTimeout.setUnits(_E)
mibBuilder.exportSymbols(_G,**{'antiTheft':antiTheft,'antiTheftMibVersion':antiTheftMibVersion,'antiTheftEnable':antiTheftEnable,'antiTheftLicense':antiTheftLicense,'antiTheftStatus':antiTheftStatus,'antiTheftTimeout':antiTheftTimeout,'antiTheftCountdown':antiTheftCountdown,'antiTheftCustomer':antiTheftCustomer,'antitheftPortMgtTable':antitheftPortMgtTable,'antitheftPortMgtEntry':antitheftPortMgtEntry,_H:antitheftPortIfIndex,'antitheftPortLock':antitheftPortLock,'antitheftPortRowStatus':antitheftPortRowStatus,'antiTheftReconnectionTimeout':antiTheftReconnectionTimeout})