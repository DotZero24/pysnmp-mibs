_E='ntcModemConfGrpV1Standard'
_D='ntcModemTxCtrlDemodLockAlarm'
_C='Integer32'
_B='NEWTEC-MODEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcModem=ModuleIdentity((1,3,6,1,4,1,5835,5,2,6500))
if mibBuilder.loadTexts:ntcModem.setRevisions(('2014-02-03 12:00',))
_NtcModemObjects_ObjectIdentity=ObjectIdentity
ntcModemObjects=_NtcModemObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,6500,1))
if mibBuilder.loadTexts:ntcModemObjects.setStatus(_A)
class _NtcModemTxCtrlDemodLockAlarm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disableTransmit',0),('noImpact',1)))
_NtcModemTxCtrlDemodLockAlarm_Type.__name__=_C
_NtcModemTxCtrlDemodLockAlarm_Object=MibScalar
ntcModemTxCtrlDemodLockAlarm=_NtcModemTxCtrlDemodLockAlarm_Object((1,3,6,1,4,1,5835,5,2,6500,1,1),_NtcModemTxCtrlDemodLockAlarm_Type())
ntcModemTxCtrlDemodLockAlarm.setMaxAccess('read-write')
if mibBuilder.loadTexts:ntcModemTxCtrlDemodLockAlarm.setStatus(_A)
_NtcModemConformance_ObjectIdentity=ObjectIdentity
ntcModemConformance=_NtcModemConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,6500,2))
if mibBuilder.loadTexts:ntcModemConformance.setStatus(_A)
_NtcModemConfCompliance_ObjectIdentity=ObjectIdentity
ntcModemConfCompliance=_NtcModemConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,6500,2,1))
if mibBuilder.loadTexts:ntcModemConfCompliance.setStatus(_A)
_NtcModemConfGroup_ObjectIdentity=ObjectIdentity
ntcModemConfGroup=_NtcModemConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,6500,2,2))
if mibBuilder.loadTexts:ntcModemConfGroup.setStatus(_A)
ntcModemConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,6500,2,2,1))
ntcModemConfGrpV1Standard.setObjects((_B,_D))
if mibBuilder.loadTexts:ntcModemConfGrpV1Standard.setStatus(_A)
ntcModemConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,6500,2,1,1))
ntcModemConfCompV1Standard.setObjects((_B,_E))
if mibBuilder.loadTexts:ntcModemConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcModem':ntcModem,'ntcModemObjects':ntcModemObjects,_D:ntcModemTxCtrlDemodLockAlarm,'ntcModemConformance':ntcModemConformance,'ntcModemConfCompliance':ntcModemConfCompliance,'ntcModemConfCompV1Standard':ntcModemConfCompV1Standard,'ntcModemConfGroup':ntcModemConfGroup,_E:ntcModemConfGrpV1Standard})