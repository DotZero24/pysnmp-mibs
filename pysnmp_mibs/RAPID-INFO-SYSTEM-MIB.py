_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rapidstream,=mibBuilder.importSymbols('RAPID-MIB','rapidstream')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
rsInfoModule=ModuleIdentity((1,3,6,1,4,1,4355,6))
if mibBuilder.loadTexts:rsInfoModule.setRevisions(('2001-04-20 12:00','2002-11-01 12:00'))
_RsInfoSystem_ObjectIdentity=ObjectIdentity
rsInfoSystem=_RsInfoSystem_ObjectIdentity((1,3,6,1,4,1,4355,6,1))
if mibBuilder.loadTexts:rsInfoSystem.setStatus(_A)
_RsInfoSystemCurrentTime_Type=DateAndTime
_RsInfoSystemCurrentTime_Object=MibScalar
rsInfoSystemCurrentTime=_RsInfoSystemCurrentTime_Object((1,3,6,1,4,1,4355,6,1,1),_RsInfoSystemCurrentTime_Type())
rsInfoSystemCurrentTime.setMaxAccess('read-only')
if mibBuilder.loadTexts:rsInfoSystemCurrentTime.setStatus(_A)
mibBuilder.exportSymbols('RAPID-INFO-SYSTEM-MIB',**{'rsInfoModule':rsInfoModule,'rsInfoSystem':rsInfoSystem,'rsInfoSystemCurrentTime':rsInfoSystemCurrentTime})