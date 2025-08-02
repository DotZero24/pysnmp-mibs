_F='lldpV2PortConfigPortNum'
_E='ARICENT-LLDP-V2-MIB'
_D='Integer32'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
LldpPortNumber,lldpExtensions=mibBuilder.importSymbols('LLDP-MIB','LldpPortNumber','lldpExtensions')
TimeFilter,=mibBuilder.importSymbols('RMON2-MIB','TimeFilter')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fslldpV2MIB=ModuleIdentity((1,0,8802,1,1,2,1,5,40001))
if mibBuilder.loadTexts:fslldpV2MIB.setRevisions(('2012-09-05 00:00',))
_LldpV2Objects_ObjectIdentity=ObjectIdentity
lldpV2Objects=_LldpV2Objects_ObjectIdentity((1,0,8802,1,1,2,1,5,40001,1))
_LldpV2Configuration_ObjectIdentity=ObjectIdentity
lldpV2Configuration=_LldpV2Configuration_ObjectIdentity((1,0,8802,1,1,2,1,5,40001,1,1))
_LldpV2RemTimeMark_Type=TimeFilter
_LldpV2RemTimeMark_Object=MibScalar
lldpV2RemTimeMark=_LldpV2RemTimeMark_Object((1,0,8802,1,1,2,1,5,40001,1,1,1),_LldpV2RemTimeMark_Type())
lldpV2RemTimeMark.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpV2RemTimeMark.setStatus(_A)
_LldpV2RemLocalIfIndex_Type=LldpPortNumber
_LldpV2RemLocalIfIndex_Object=MibScalar
lldpV2RemLocalIfIndex=_LldpV2RemLocalIfIndex_Object((1,0,8802,1,1,2,1,5,40001,1,1,2),_LldpV2RemLocalIfIndex_Type())
lldpV2RemLocalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpV2RemLocalIfIndex.setStatus(_A)
_LldpV2LocPortIfIndex_Type=LldpPortNumber
_LldpV2LocPortIfIndex_Object=MibScalar
lldpV2LocPortIfIndex=_LldpV2LocPortIfIndex_Object((1,0,8802,1,1,2,1,5,40001,1,1,3),_LldpV2LocPortIfIndex_Type())
lldpV2LocPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpV2LocPortIfIndex.setStatus(_A)
class _LldpV2RemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpV2RemIndex_Type.__name__=_D
_LldpV2RemIndex_Object=MibScalar
lldpV2RemIndex=_LldpV2RemIndex_Object((1,0,8802,1,1,2,1,5,40001,1,1,4),_LldpV2RemIndex_Type())
lldpV2RemIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpV2RemIndex.setStatus(_A)
class _LldpV2RemLocalDestMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_LldpV2RemLocalDestMACAddress_Type.__name__=_C
_LldpV2RemLocalDestMACAddress_Object=MibScalar
lldpV2RemLocalDestMACAddress=_LldpV2RemLocalDestMACAddress_Object((1,0,8802,1,1,2,1,5,40001,1,1,5),_LldpV2RemLocalDestMACAddress_Type())
lldpV2RemLocalDestMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpV2RemLocalDestMACAddress.setStatus(_A)
_LldpV2PortConfigTable_Object=MibTable
lldpV2PortConfigTable=_LldpV2PortConfigTable_Object((1,0,8802,1,1,2,1,5,40001,1,1,6))
if mibBuilder.loadTexts:lldpV2PortConfigTable.setStatus(_A)
_LldpV2PortConfigEntry_Object=MibTableRow
lldpV2PortConfigEntry=_LldpV2PortConfigEntry_Object((1,0,8802,1,1,2,1,5,40001,1,1,6,1))
lldpV2PortConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:lldpV2PortConfigEntry.setStatus(_A)
_LldpV2PortConfigPortNum_Type=LldpPortNumber
_LldpV2PortConfigPortNum_Object=MibTableColumn
lldpV2PortConfigPortNum=_LldpV2PortConfigPortNum_Object((1,0,8802,1,1,2,1,5,40001,1,1,6,1,1),_LldpV2PortConfigPortNum_Type())
lldpV2PortConfigPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpV2PortConfigPortNum.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fslldpV2MIB':fslldpV2MIB,'lldpV2Objects':lldpV2Objects,'lldpV2Configuration':lldpV2Configuration,'lldpV2RemTimeMark':lldpV2RemTimeMark,'lldpV2RemLocalIfIndex':lldpV2RemLocalIfIndex,'lldpV2LocPortIfIndex':lldpV2LocPortIfIndex,'lldpV2RemIndex':lldpV2RemIndex,'lldpV2RemLocalDestMACAddress':lldpV2RemLocalDestMACAddress,'lldpV2PortConfigTable':lldpV2PortConfigTable,'lldpV2PortConfigEntry':lldpV2PortConfigEntry,_F:lldpV2PortConfigPortNum})