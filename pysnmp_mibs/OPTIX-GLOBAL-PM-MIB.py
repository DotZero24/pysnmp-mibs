_F='pmHistCtrPeriod'
_E='OPTIX-GLOBAL-PM-MIB'
_D='2008-05-24 00:00'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AlarmEventType,AlmDataNtfcnCdeType,AlmDataSrvEffType,ObjType,PerformanceEventType,ValidflagType=mibBuilder.importSymbols('OPTIX-GLOBAL-TC-MIB','AlarmEventType','AlmDataNtfcnCdeType','AlmDataSrvEffType','ObjType','PerformanceEventType','ValidflagType')
optixCommonGlobal,=mibBuilder.importSymbols('OPTIX-OID-MIB','optixCommonGlobal')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
optixGlobalPM=ModuleIdentity((1,3,6,1,4,1,2011,2,25,3,40,10))
if mibBuilder.loadTexts:optixGlobalPM.setRevisions((_D,))
optixGlobalPER=ModuleIdentity((1,3,6,1,4,1,2011,2,25,3,40,20))
if mibBuilder.loadTexts:optixGlobalPER.setRevisions((_D,))
_PmHistCtr_ObjectIdentity=ObjectIdentity
pmHistCtr=_PmHistCtr_ObjectIdentity((1,3,6,1,4,1,2011,2,25,3,40,10,10))
_PmHistCtrTable_Object=MibTable
pmHistCtrTable=_PmHistCtrTable_Object((1,3,6,1,4,1,2011,2,25,3,40,10,10,10))
if mibBuilder.loadTexts:pmHistCtrTable.setStatus(_A)
_PmHistCtrEntry_Object=MibTableRow
pmHistCtrEntry=_PmHistCtrEntry_Object((1,3,6,1,4,1,2011,2,25,3,40,10,10,10,1))
pmHistCtrEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:pmHistCtrEntry.setStatus(_A)
class _PmHistCtrPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(17,18,19,20)));namedValues=NamedValues(*(('period30s',17),('period30m',18),('periodPrdvar',19),('periodPrdvar2',20)))
_PmHistCtrPeriod_Type.__name__=_B
_PmHistCtrPeriod_Object=MibTableColumn
pmHistCtrPeriod=_PmHistCtrPeriod_Object((1,3,6,1,4,1,2011,2,25,3,40,10,10,10,1,1),_PmHistCtrPeriod_Type())
pmHistCtrPeriod.setMaxAccess('read-only')
if mibBuilder.loadTexts:pmHistCtrPeriod.setStatus(_A)
_PmHistCtrRecNum_Type=Integer32
_PmHistCtrRecNum_Object=MibTableColumn
pmHistCtrRecNum=_PmHistCtrRecNum_Object((1,3,6,1,4,1,2011,2,25,3,40,10,10,10,1,2),_PmHistCtrRecNum_Type())
pmHistCtrRecNum.setMaxAccess(_C)
if mibBuilder.loadTexts:pmHistCtrRecNum.setStatus(_A)
_PmHistCtrInterval_Type=Integer32
_PmHistCtrInterval_Object=MibTableColumn
pmHistCtrInterval=_PmHistCtrInterval_Object((1,3,6,1,4,1,2011,2,25,3,40,10,10,10,1,3),_PmHistCtrInterval_Type())
pmHistCtrInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:pmHistCtrInterval.setStatus(_A)
class _PmHistCtrEnableFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_PmHistCtrEnableFlag_Type.__name__=_B
_PmHistCtrEnableFlag_Object=MibTableColumn
pmHistCtrEnableFlag=_PmHistCtrEnableFlag_Object((1,3,6,1,4,1,2011,2,25,3,40,10,10,10,1,4),_PmHistCtrEnableFlag_Type())
pmHistCtrEnableFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:pmHistCtrEnableFlag.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'optixGlobalPM':optixGlobalPM,'pmHistCtr':pmHistCtr,'pmHistCtrTable':pmHistCtrTable,'pmHistCtrEntry':pmHistCtrEntry,_F:pmHistCtrPeriod,'pmHistCtrRecNum':pmHistCtrRecNum,'pmHistCtrInterval':pmHistCtrInterval,'pmHistCtrEnableFlag':pmHistCtrEnableFlag,'optixGlobalPER':optixGlobalPER})