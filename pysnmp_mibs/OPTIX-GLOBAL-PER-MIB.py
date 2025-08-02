_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MOD2Type,PerformanceEventType,ValidflagType=mibBuilder.importSymbols('OPTIX-GLOBAL-TC-MIB','MOD2Type','PerformanceEventType','ValidflagType')
optixCommonGlobal,=mibBuilder.importSymbols('OPTIX-OID-MIB','optixCommonGlobal')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
optixGlobalPER=ModuleIdentity((1,3,6,1,4,1,2011,2,25,3,40,20))
if mibBuilder.loadTexts:optixGlobalPER.setRevisions(('2008-05-24 00:00',))
_PerMonitorTime_ObjectIdentity=ObjectIdentity
perMonitorTime=_PerMonitorTime_ObjectIdentity((1,3,6,1,4,1,2011,2,25,3,40,20,10))
_Per15mMonitorTime_ObjectIdentity=ObjectIdentity
per15mMonitorTime=_Per15mMonitorTime_ObjectIdentity((1,3,6,1,4,1,2011,2,25,3,40,20,10,10))
_Per15mMonitorStartTime_Type=DateAndTime
_Per15mMonitorStartTime_Object=MibScalar
per15mMonitorStartTime=_Per15mMonitorStartTime_Object((1,3,6,1,4,1,2011,2,25,3,40,20,10,10,10),_Per15mMonitorStartTime_Type())
per15mMonitorStartTime.setMaxAccess(_A)
if mibBuilder.loadTexts:per15mMonitorStartTime.setStatus(_B)
_Per15mMonitorEndTime_Type=DateAndTime
_Per15mMonitorEndTime_Object=MibScalar
per15mMonitorEndTime=_Per15mMonitorEndTime_Object((1,3,6,1,4,1,2011,2,25,3,40,20,10,10,20),_Per15mMonitorEndTime_Type())
per15mMonitorEndTime.setMaxAccess(_A)
if mibBuilder.loadTexts:per15mMonitorEndTime.setStatus(_B)
_Per24hMonitorTime_ObjectIdentity=ObjectIdentity
per24hMonitorTime=_Per24hMonitorTime_ObjectIdentity((1,3,6,1,4,1,2011,2,25,3,40,20,10,20))
_Per24hMonitorStartTime_Type=DateAndTime
_Per24hMonitorStartTime_Object=MibScalar
per24hMonitorStartTime=_Per24hMonitorStartTime_Object((1,3,6,1,4,1,2011,2,25,3,40,20,10,20,10),_Per24hMonitorStartTime_Type())
per24hMonitorStartTime.setMaxAccess(_A)
if mibBuilder.loadTexts:per24hMonitorStartTime.setStatus(_B)
_Per24hMonitorEndTime_Type=DateAndTime
_Per24hMonitorEndTime_Object=MibScalar
per24hMonitorEndTime=_Per24hMonitorEndTime_Object((1,3,6,1,4,1,2011,2,25,3,40,20,10,20,20),_Per24hMonitorEndTime_Type())
per24hMonitorEndTime.setMaxAccess(_A)
if mibBuilder.loadTexts:per24hMonitorEndTime.setStatus(_B)
mibBuilder.exportSymbols('OPTIX-GLOBAL-PER-MIB',**{'optixGlobalPER':optixGlobalPER,'perMonitorTime':perMonitorTime,'per15mMonitorTime':per15mMonitorTime,'per15mMonitorStartTime':per15mMonitorStartTime,'per15mMonitorEndTime':per15mMonitorEndTime,'per24hMonitorTime':per24hMonitorTime,'per24hMonitorStartTime':per24hMonitorStartTime,'per24hMonitorEndTime':per24hMonitorEndTime})