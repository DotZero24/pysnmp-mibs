_J='stacking'
_I='standalone'
_H='read-only'
_G='bayStackUnitConfigIndex'
_F='BAY-STACK-MIB'
_E='TruthValue'
_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackMib=ModuleIdentity((1,3,6,1,4,1,45,5,13))
if mibBuilder.loadTexts:bayStackMib.setRevisions(('2021-02-09 00:00','2013-10-11 00:00','2012-10-02 00:00','2009-09-28 00:00','2007-09-04 00:00','2005-08-22 00:00'))
_BayStackObjects_ObjectIdentity=ObjectIdentity
bayStackObjects=_BayStackObjects_ObjectIdentity((1,3,6,1,4,1,45,5,13,1))
_BayStackConfig_ObjectIdentity=ObjectIdentity
bayStackConfig=_BayStackConfig_ObjectIdentity((1,3,6,1,4,1,45,5,13,1,1))
class _BayStackConfigExpectedStackSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BayStackConfigExpectedStackSize_Type.__name__=_C
_BayStackConfigExpectedStackSize_Object=MibScalar
bayStackConfigExpectedStackSize=_BayStackConfigExpectedStackSize_Object((1,3,6,1,4,1,45,5,13,1,1,1),_BayStackConfigExpectedStackSize_Type())
bayStackConfigExpectedStackSize.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackConfigExpectedStackSize.setStatus(_A)
class _BayStackConfigStackErrorNotificationInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BayStackConfigStackErrorNotificationInterval_Type.__name__=_C
_BayStackConfigStackErrorNotificationInterval_Object=MibScalar
bayStackConfigStackErrorNotificationInterval=_BayStackConfigStackErrorNotificationInterval_Object((1,3,6,1,4,1,45,5,13,1,1,2),_BayStackConfigStackErrorNotificationInterval_Type())
bayStackConfigStackErrorNotificationInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackConfigStackErrorNotificationInterval.setStatus(_A)
if mibBuilder.loadTexts:bayStackConfigStackErrorNotificationInterval.setUnits('Seconds')
_BayStackConfigStackErrorNotificationEnabled_Type=TruthValue
_BayStackConfigStackErrorNotificationEnabled_Object=MibScalar
bayStackConfigStackErrorNotificationEnabled=_BayStackConfigStackErrorNotificationEnabled_Object((1,3,6,1,4,1,45,5,13,1,1,3),_BayStackConfigStackErrorNotificationEnabled_Type())
bayStackConfigStackErrorNotificationEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackConfigStackErrorNotificationEnabled.setStatus(_A)
_BayStackConfigStackRebootUnitOnFailure_Type=TruthValue
_BayStackConfigStackRebootUnitOnFailure_Object=MibScalar
bayStackConfigStackRebootUnitOnFailure=_BayStackConfigStackRebootUnitOnFailure_Object((1,3,6,1,4,1,45,5,13,1,1,4),_BayStackConfigStackRebootUnitOnFailure_Type())
bayStackConfigStackRebootUnitOnFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackConfigStackRebootUnitOnFailure.setStatus(_A)
class _BayStackConfigStackRetryCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_BayStackConfigStackRetryCount_Type.__name__=_D
_BayStackConfigStackRetryCount_Object=MibScalar
bayStackConfigStackRetryCount=_BayStackConfigStackRetryCount_Object((1,3,6,1,4,1,45,5,13,1,1,5),_BayStackConfigStackRetryCount_Type())
bayStackConfigStackRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackConfigStackRetryCount.setStatus(_A)
class _BaystackConfigTcpKeepaliveEnable_Type(TruthValue):defaultValue=2
_BaystackConfigTcpKeepaliveEnable_Type.__name__=_E
_BaystackConfigTcpKeepaliveEnable_Object=MibScalar
baystackConfigTcpKeepaliveEnable=_BaystackConfigTcpKeepaliveEnable_Object((1,3,6,1,4,1,45,5,13,1,1,6),_BaystackConfigTcpKeepaliveEnable_Type())
baystackConfigTcpKeepaliveEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:baystackConfigTcpKeepaliveEnable.setStatus(_A)
class _BaystackConfigTcpKeepaliveInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_BaystackConfigTcpKeepaliveInterval_Type.__name__=_C
_BaystackConfigTcpKeepaliveInterval_Object=MibScalar
baystackConfigTcpKeepaliveInterval=_BaystackConfigTcpKeepaliveInterval_Object((1,3,6,1,4,1,45,5,13,1,1,7),_BaystackConfigTcpKeepaliveInterval_Type())
baystackConfigTcpKeepaliveInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:baystackConfigTcpKeepaliveInterval.setStatus(_A)
class _BaystackConfigTcpKeepaliveRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_BaystackConfigTcpKeepaliveRetries_Type.__name__=_C
_BaystackConfigTcpKeepaliveRetries_Object=MibScalar
baystackConfigTcpKeepaliveRetries=_BaystackConfigTcpKeepaliveRetries_Object((1,3,6,1,4,1,45,5,13,1,1,8),_BaystackConfigTcpKeepaliveRetries_Type())
baystackConfigTcpKeepaliveRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:baystackConfigTcpKeepaliveRetries.setStatus(_A)
_BayStackUnitConfigTable_Object=MibTable
bayStackUnitConfigTable=_BayStackUnitConfigTable_Object((1,3,6,1,4,1,45,5,13,1,2))
if mibBuilder.loadTexts:bayStackUnitConfigTable.setStatus(_A)
_BayStackUnitConfigEntry_Object=MibTableRow
bayStackUnitConfigEntry=_BayStackUnitConfigEntry_Object((1,3,6,1,4,1,45,5,13,1,2,1))
bayStackUnitConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:bayStackUnitConfigEntry.setStatus(_A)
class _BayStackUnitConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BayStackUnitConfigIndex_Type.__name__=_C
_BayStackUnitConfigIndex_Object=MibTableColumn
bayStackUnitConfigIndex=_BayStackUnitConfigIndex_Object((1,3,6,1,4,1,45,5,13,1,2,1,1),_BayStackUnitConfigIndex_Type())
bayStackUnitConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:bayStackUnitConfigIndex.setStatus(_A)
class _BayStackUnitConfigRearPortAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('spb',3)))
_BayStackUnitConfigRearPortAdminMode_Type.__name__=_C
_BayStackUnitConfigRearPortAdminMode_Object=MibTableColumn
bayStackUnitConfigRearPortAdminMode=_BayStackUnitConfigRearPortAdminMode_Object((1,3,6,1,4,1,45,5,13,1,2,1,2),_BayStackUnitConfigRearPortAdminMode_Type())
bayStackUnitConfigRearPortAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackUnitConfigRearPortAdminMode.setStatus(_A)
class _BayStackUnitConfigRearPortOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('spb',3)))
_BayStackUnitConfigRearPortOperMode_Type.__name__=_C
_BayStackUnitConfigRearPortOperMode_Object=MibTableColumn
bayStackUnitConfigRearPortOperMode=_BayStackUnitConfigRearPortOperMode_Object((1,3,6,1,4,1,45,5,13,1,2,1,3),_BayStackUnitConfigRearPortOperMode_Type())
bayStackUnitConfigRearPortOperMode.setMaxAccess(_H)
if mibBuilder.loadTexts:bayStackUnitConfigRearPortOperMode.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'bayStackMib':bayStackMib,'bayStackObjects':bayStackObjects,'bayStackConfig':bayStackConfig,'bayStackConfigExpectedStackSize':bayStackConfigExpectedStackSize,'bayStackConfigStackErrorNotificationInterval':bayStackConfigStackErrorNotificationInterval,'bayStackConfigStackErrorNotificationEnabled':bayStackConfigStackErrorNotificationEnabled,'bayStackConfigStackRebootUnitOnFailure':bayStackConfigStackRebootUnitOnFailure,'bayStackConfigStackRetryCount':bayStackConfigStackRetryCount,'baystackConfigTcpKeepaliveEnable':baystackConfigTcpKeepaliveEnable,'baystackConfigTcpKeepaliveInterval':baystackConfigTcpKeepaliveInterval,'baystackConfigTcpKeepaliveRetries':baystackConfigTcpKeepaliveRetries,'bayStackUnitConfigTable':bayStackUnitConfigTable,'bayStackUnitConfigEntry':bayStackUnitConfigEntry,_G:bayStackUnitConfigIndex,'bayStackUnitConfigRearPortAdminMode':bayStackUnitConfigRearPortAdminMode,'bayStackUnitConfigRearPortOperMode':bayStackUnitConfigRearPortOperMode})