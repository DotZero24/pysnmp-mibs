_E='eltIpUnnumberedIfIndex'
_D='ELTEX-MES-VLAN-AGGREGATE-MIB'
_C='read-write'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
eltMesIpUnnumbered=ModuleIdentity((1,3,6,1,4,1,35265,1,23,7))
if mibBuilder.loadTexts:eltMesIpUnnumbered.setRevisions(('2014-05-23 00:00',))
_EltIpUnnumberedInterfaceTable_Object=MibTable
eltIpUnnumberedInterfaceTable=_EltIpUnnumberedInterfaceTable_Object((1,3,6,1,4,1,35265,1,23,7,1))
if mibBuilder.loadTexts:eltIpUnnumberedInterfaceTable.setStatus(_A)
_EltIpUnnumberedInterfaceEntry_Object=MibTableRow
eltIpUnnumberedInterfaceEntry=_EltIpUnnumberedInterfaceEntry_Object((1,3,6,1,4,1,35265,1,23,7,1,1))
eltIpUnnumberedInterfaceEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:eltIpUnnumberedInterfaceEntry.setStatus(_A)
_EltIpUnnumberedIfIndex_Type=Integer32
_EltIpUnnumberedIfIndex_Object=MibTableColumn
eltIpUnnumberedIfIndex=_EltIpUnnumberedIfIndex_Object((1,3,6,1,4,1,35265,1,23,7,1,1,1),_EltIpUnnumberedIfIndex_Type())
eltIpUnnumberedIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpUnnumberedIfIndex.setStatus(_A)
_EltIpUnnumberedAggrIfIndex_Type=Integer32
_EltIpUnnumberedAggrIfIndex_Object=MibTableColumn
eltIpUnnumberedAggrIfIndex=_EltIpUnnumberedAggrIfIndex_Object((1,3,6,1,4,1,35265,1,23,7,1,1,2),_EltIpUnnumberedAggrIfIndex_Type())
eltIpUnnumberedAggrIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:eltIpUnnumberedAggrIfIndex.setStatus(_A)
class _EltIpUnnumberedVlan1to1024_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltIpUnnumberedVlan1to1024_Type.__name__=_B
_EltIpUnnumberedVlan1to1024_Object=MibTableColumn
eltIpUnnumberedVlan1to1024=_EltIpUnnumberedVlan1to1024_Object((1,3,6,1,4,1,35265,1,23,7,1,1,3),_EltIpUnnumberedVlan1to1024_Type())
eltIpUnnumberedVlan1to1024.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpUnnumberedVlan1to1024.setStatus(_A)
class _EltIpUnnumberedVlan1025to2048_Type(OctetString):defaultHexValue='00';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltIpUnnumberedVlan1025to2048_Type.__name__=_B
_EltIpUnnumberedVlan1025to2048_Object=MibTableColumn
eltIpUnnumberedVlan1025to2048=_EltIpUnnumberedVlan1025to2048_Object((1,3,6,1,4,1,35265,1,23,7,1,1,4),_EltIpUnnumberedVlan1025to2048_Type())
eltIpUnnumberedVlan1025to2048.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpUnnumberedVlan1025to2048.setStatus(_A)
class _EltIpUnnumberedVlan2049to3072_Type(OctetString):defaultHexValue='00';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltIpUnnumberedVlan2049to3072_Type.__name__=_B
_EltIpUnnumberedVlan2049to3072_Object=MibTableColumn
eltIpUnnumberedVlan2049to3072=_EltIpUnnumberedVlan2049to3072_Object((1,3,6,1,4,1,35265,1,23,7,1,1,5),_EltIpUnnumberedVlan2049to3072_Type())
eltIpUnnumberedVlan2049to3072.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpUnnumberedVlan2049to3072.setStatus(_A)
class _EltIpUnnumberedVlan3073to4094_Type(OctetString):defaultHexValue='00';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltIpUnnumberedVlan3073to4094_Type.__name__=_B
_EltIpUnnumberedVlan3073to4094_Object=MibTableColumn
eltIpUnnumberedVlan3073to4094=_EltIpUnnumberedVlan3073to4094_Object((1,3,6,1,4,1,35265,1,23,7,1,1,6),_EltIpUnnumberedVlan3073to4094_Type())
eltIpUnnumberedVlan3073to4094.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpUnnumberedVlan3073to4094.setStatus(_A)
_EltIpUnnumberedStatus_Type=RowStatus
_EltIpUnnumberedStatus_Object=MibTableColumn
eltIpUnnumberedStatus=_EltIpUnnumberedStatus_Object((1,3,6,1,4,1,35265,1,23,7,1,1,7),_EltIpUnnumberedStatus_Type())
eltIpUnnumberedStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:eltIpUnnumberedStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'eltMesIpUnnumbered':eltMesIpUnnumbered,'eltIpUnnumberedInterfaceTable':eltIpUnnumberedInterfaceTable,'eltIpUnnumberedInterfaceEntry':eltIpUnnumberedInterfaceEntry,_E:eltIpUnnumberedIfIndex,'eltIpUnnumberedAggrIfIndex':eltIpUnnumberedAggrIfIndex,'eltIpUnnumberedVlan1to1024':eltIpUnnumberedVlan1to1024,'eltIpUnnumberedVlan1025to2048':eltIpUnnumberedVlan1025to2048,'eltIpUnnumberedVlan2049to3072':eltIpUnnumberedVlan2049to3072,'eltIpUnnumberedVlan3073to4094':eltIpUnnumberedVlan3073to4094,'eltIpUnnumberedStatus':eltIpUnnumberedStatus})