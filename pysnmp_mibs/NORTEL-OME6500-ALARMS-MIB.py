_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ome6500,=mibBuilder.importSymbols('NORTEL-OPTICAL-OME6500-MIB','ome6500')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
nnOme6500Alarms=ModuleIdentity((1,3,6,1,4,1,562,68,11,4))
if mibBuilder.loadTexts:nnOme6500Alarms.setRevisions(('2007-02-02 00:00','2008-02-07 00:00','2009-06-15 00:00'))
_NnOme6500AlarmCounts_ObjectIdentity=ObjectIdentity
nnOme6500AlarmCounts=_NnOme6500AlarmCounts_ObjectIdentity((1,3,6,1,4,1,562,68,11,4,1))
_Critical_Type=Integer32
_Critical_Object=MibScalar
critical=_Critical_Object((1,3,6,1,4,1,562,68,11,4,1,1),_Critical_Type())
critical.setMaxAccess(_A)
if mibBuilder.loadTexts:critical.setStatus(_B)
_Major_Type=Integer32
_Major_Object=MibScalar
major=_Major_Object((1,3,6,1,4,1,562,68,11,4,1,2),_Major_Type())
major.setMaxAccess(_A)
if mibBuilder.loadTexts:major.setStatus(_B)
_Minor_Type=Integer32
_Minor_Object=MibScalar
minor=_Minor_Object((1,3,6,1,4,1,562,68,11,4,1,3),_Minor_Type())
minor.setMaxAccess(_A)
if mibBuilder.loadTexts:minor.setStatus(_B)
_Warnings_Type=Integer32
_Warnings_Object=MibScalar
warnings=_Warnings_Object((1,3,6,1,4,1,562,68,11,4,1,4),_Warnings_Type())
warnings.setMaxAccess(_A)
if mibBuilder.loadTexts:warnings.setStatus(_B)
_LastAlarmTimeStamp_Type=DateAndTime
_LastAlarmTimeStamp_Object=MibScalar
lastAlarmTimeStamp=_LastAlarmTimeStamp_Object((1,3,6,1,4,1,562,68,11,4,1,5),_LastAlarmTimeStamp_Type())
lastAlarmTimeStamp.setMaxAccess(_A)
if mibBuilder.loadTexts:lastAlarmTimeStamp.setStatus(_B)
mibBuilder.exportSymbols('NORTEL-OME6500-ALARMS-MIB',**{'nnOme6500Alarms':nnOme6500Alarms,'nnOme6500AlarmCounts':nnOme6500AlarmCounts,'critical':critical,'major':major,'minor':minor,'warnings':warnings,'lastAlarmTimeStamp':lastAlarmTimeStamp})