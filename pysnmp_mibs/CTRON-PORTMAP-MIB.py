_F='portMapIndex'
_E='CTRON-PORTMAP-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctPortMap,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctPortMap')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_PortMap_ObjectIdentity=ObjectIdentity
portMap=_PortMap_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,16,1))
_PortMapTable_Object=MibTable
portMapTable=_PortMapTable_Object((1,3,6,1,4,1,52,4,1,1,16,1,1))
if mibBuilder.loadTexts:portMapTable.setStatus(_A)
_PortMapEntry_Object=MibTableRow
portMapEntry=_PortMapEntry_Object((1,3,6,1,4,1,52,4,1,1,16,1,1,1))
portMapEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:portMapEntry.setStatus(_A)
_PortMapIndex_Type=Integer32
_PortMapIndex_Object=MibTableColumn
portMapIndex=_PortMapIndex_Object((1,3,6,1,4,1,52,4,1,1,16,1,1,1,1),_PortMapIndex_Type())
portMapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portMapIndex.setStatus(_A)
_PortMapRepeater_Type=Integer32
_PortMapRepeater_Object=MibTableColumn
portMapRepeater=_PortMapRepeater_Object((1,3,6,1,4,1,52,4,1,1,16,1,1,1,2),_PortMapRepeater_Type())
portMapRepeater.setMaxAccess(_B)
if mibBuilder.loadTexts:portMapRepeater.setStatus(_A)
class _PortMapCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_PortMapCapability_Type.__name__=_C
_PortMapCapability_Object=MibTableColumn
portMapCapability=_PortMapCapability_Object((1,3,6,1,4,1,52,4,1,1,16,1,1,1,3),_PortMapCapability_Type())
portMapCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:portMapCapability.setStatus(_A)
class _PortMapOperationalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_PortMapOperationalMode_Type.__name__=_C
_PortMapOperationalMode_Object=MibTableColumn
portMapOperationalMode=_PortMapOperationalMode_Object((1,3,6,1,4,1,52,4,1,1,16,1,1,1,4),_PortMapOperationalMode_Type())
portMapOperationalMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:portMapOperationalMode.setStatus(_A)
class _PortMapLastSeenSrcAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_PortMapLastSeenSrcAddr_Type.__name__=_D
_PortMapLastSeenSrcAddr_Object=MibTableColumn
portMapLastSeenSrcAddr=_PortMapLastSeenSrcAddr_Object((1,3,6,1,4,1,52,4,1,1,16,1,1,1,5),_PortMapLastSeenSrcAddr_Type())
portMapLastSeenSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:portMapLastSeenSrcAddr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'portMap':portMap,'portMapTable':portMapTable,'portMapEntry':portMapEntry,_F:portMapIndex,'portMapRepeater':portMapRepeater,'portMapCapability':portMapCapability,'portMapOperationalMode':portMapOperationalMode,'portMapLastSeenSrcAddr':portMapLastSeenSrcAddr})