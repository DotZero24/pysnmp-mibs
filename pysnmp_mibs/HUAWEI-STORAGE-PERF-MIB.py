_D='hwPerfDiskIndex'
_C='HUAWEI-STORAGE-PERF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Huawei_ObjectIdentity=ObjectIdentity
huawei=_Huawei_ObjectIdentity((1,3,6,1,4,1,2011))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,2011,2))
_Storage_ObjectIdentity=ObjectIdentity
storage=_Storage_ObjectIdentity((1,3,6,1,4,1,2011,2,251))
_Performance_ObjectIdentity=ObjectIdentity
performance=_Performance_ObjectIdentity((1,3,6,1,4,1,2011,2,251,21))
_HwPerfDiskTable_Object=MibTable
hwPerfDiskTable=_HwPerfDiskTable_Object((1,3,6,1,4,1,2011,2,251,21,10))
if mibBuilder.loadTexts:hwPerfDiskTable.setStatus(_A)
_HwPerfDiskEntry_Object=MibTableRow
hwPerfDiskEntry=_HwPerfDiskEntry_Object((1,3,6,1,4,1,2011,2,251,21,10,1))
hwPerfDiskEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hwPerfDiskEntry.setStatus(_A)
_HwPerfDiskIndex_Type=OctetString
_HwPerfDiskIndex_Object=MibTableColumn
hwPerfDiskIndex=_HwPerfDiskIndex_Object((1,3,6,1,4,1,2011,2,251,21,10,1,1),_HwPerfDiskIndex_Type())
hwPerfDiskIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPerfDiskIndex.setStatus(_A)
_HwPerfDiskTotalIOPS_Type=Unsigned32
_HwPerfDiskTotalIOPS_Object=MibTableColumn
hwPerfDiskTotalIOPS=_HwPerfDiskTotalIOPS_Object((1,3,6,1,4,1,2011,2,251,21,10,1,2),_HwPerfDiskTotalIOPS_Type())
hwPerfDiskTotalIOPS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPerfDiskTotalIOPS.setStatus(_A)
_HwPerfDiskReadIOPS_Type=Unsigned32
_HwPerfDiskReadIOPS_Object=MibTableColumn
hwPerfDiskReadIOPS=_HwPerfDiskReadIOPS_Object((1,3,6,1,4,1,2011,2,251,21,10,1,3),_HwPerfDiskReadIOPS_Type())
hwPerfDiskReadIOPS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPerfDiskReadIOPS.setStatus(_A)
_HwPerfDiskWriteIOPS_Type=Unsigned32
_HwPerfDiskWriteIOPS_Object=MibTableColumn
hwPerfDiskWriteIOPS=_HwPerfDiskWriteIOPS_Object((1,3,6,1,4,1,2011,2,251,21,10,1,4),_HwPerfDiskWriteIOPS_Type())
hwPerfDiskWriteIOPS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPerfDiskWriteIOPS.setStatus(_A)
_HwPerfDiskTotalTraffic_Type=Counter64
_HwPerfDiskTotalTraffic_Object=MibTableColumn
hwPerfDiskTotalTraffic=_HwPerfDiskTotalTraffic_Object((1,3,6,1,4,1,2011,2,251,21,10,1,5),_HwPerfDiskTotalTraffic_Type())
hwPerfDiskTotalTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPerfDiskTotalTraffic.setStatus(_A)
_HwPerfDiskReadTraffic_Type=Counter64
_HwPerfDiskReadTraffic_Object=MibTableColumn
hwPerfDiskReadTraffic=_HwPerfDiskReadTraffic_Object((1,3,6,1,4,1,2011,2,251,21,10,1,6),_HwPerfDiskReadTraffic_Type())
hwPerfDiskReadTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPerfDiskReadTraffic.setStatus(_A)
_HwPerfDiskWriteTraffic_Type=Counter64
_HwPerfDiskWriteTraffic_Object=MibTableColumn
hwPerfDiskWriteTraffic=_HwPerfDiskWriteTraffic_Object((1,3,6,1,4,1,2011,2,251,21,10,1,7),_HwPerfDiskWriteTraffic_Type())
hwPerfDiskWriteTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPerfDiskWriteTraffic.setStatus(_A)
_HwPerfDiskDelay_Type=Counter64
_HwPerfDiskDelay_Object=MibTableColumn
hwPerfDiskDelay=_HwPerfDiskDelay_Object((1,3,6,1,4,1,2011,2,251,21,10,1,8),_HwPerfDiskDelay_Type())
hwPerfDiskDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPerfDiskDelay.setStatus(_A)
_HwPerfDiskLengthOfQueue_Type=Unsigned32
_HwPerfDiskLengthOfQueue_Object=MibTableColumn
hwPerfDiskLengthOfQueue=_HwPerfDiskLengthOfQueue_Object((1,3,6,1,4,1,2011,2,251,21,10,1,9),_HwPerfDiskLengthOfQueue_Type())
hwPerfDiskLengthOfQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPerfDiskLengthOfQueue.setStatus(_A)
_HwPerfDiskAverageIO_Type=Unsigned32
_HwPerfDiskAverageIO_Object=MibTableColumn
hwPerfDiskAverageIO=_HwPerfDiskAverageIO_Object((1,3,6,1,4,1,2011,2,251,21,10,1,11),_HwPerfDiskAverageIO_Type())
hwPerfDiskAverageIO.setMaxAccess('read-write')
if mibBuilder.loadTexts:hwPerfDiskAverageIO.setStatus(_A)
_HwPerfDiskAverageReadIO_Type=Unsigned32
_HwPerfDiskAverageReadIO_Object=MibTableColumn
hwPerfDiskAverageReadIO=_HwPerfDiskAverageReadIO_Object((1,3,6,1,4,1,2011,2,251,21,10,1,12),_HwPerfDiskAverageReadIO_Type())
hwPerfDiskAverageReadIO.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPerfDiskAverageReadIO.setStatus(_A)
_HwPerfDiskAverageWriteIO_Type=Unsigned32
_HwPerfDiskAverageWriteIO_Object=MibTableColumn
hwPerfDiskAverageWriteIO=_HwPerfDiskAverageWriteIO_Object((1,3,6,1,4,1,2011,2,251,21,10,1,13),_HwPerfDiskAverageWriteIO_Type())
hwPerfDiskAverageWriteIO.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPerfDiskAverageWriteIO.setStatus(_A)
_HwPerfDiskMaxIOPS_Type=Unsigned32
_HwPerfDiskMaxIOPS_Object=MibTableColumn
hwPerfDiskMaxIOPS=_HwPerfDiskMaxIOPS_Object((1,3,6,1,4,1,2011,2,251,21,10,1,14),_HwPerfDiskMaxIOPS_Type())
hwPerfDiskMaxIOPS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPerfDiskMaxIOPS.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'huawei':huawei,'products':products,'storage':storage,'performance':performance,'hwPerfDiskTable':hwPerfDiskTable,'hwPerfDiskEntry':hwPerfDiskEntry,_D:hwPerfDiskIndex,'hwPerfDiskTotalIOPS':hwPerfDiskTotalIOPS,'hwPerfDiskReadIOPS':hwPerfDiskReadIOPS,'hwPerfDiskWriteIOPS':hwPerfDiskWriteIOPS,'hwPerfDiskTotalTraffic':hwPerfDiskTotalTraffic,'hwPerfDiskReadTraffic':hwPerfDiskReadTraffic,'hwPerfDiskWriteTraffic':hwPerfDiskWriteTraffic,'hwPerfDiskDelay':hwPerfDiskDelay,'hwPerfDiskLengthOfQueue':hwPerfDiskLengthOfQueue,'hwPerfDiskAverageIO':hwPerfDiskAverageIO,'hwPerfDiskAverageReadIO':hwPerfDiskAverageReadIO,'hwPerfDiskAverageWriteIO':hwPerfDiskAverageWriteIO,'hwPerfDiskMaxIOPS':hwPerfDiskMaxIOPS})