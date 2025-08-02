_F='ifIndex'
_E='IF-MIB'
_D='HmEnabledStatus'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_D,'hm2ConfigurationMibs')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2LLDPMib=ModuleIdentity((1,3,6,1,4,1,248,11,34))
if mibBuilder.loadTexts:hm2LLDPMib.setRevisions(('2011-04-11 00:00',))
_Hm2LLDPMibObjects_ObjectIdentity=ObjectIdentity
hm2LLDPMibObjects=_Hm2LLDPMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,34,1))
_Hm2LLDPConfigGroup_ObjectIdentity=ObjectIdentity
hm2LLDPConfigGroup=_Hm2LLDPConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,34,1,1))
class _Hm2LLDPAdminStatus_Type(HmEnabledStatus):defaultValue=1
_Hm2LLDPAdminStatus_Type.__name__=_D
_Hm2LLDPAdminStatus_Object=MibScalar
hm2LLDPAdminStatus=_Hm2LLDPAdminStatus_Object((1,3,6,1,4,1,248,11,34,1,1,1),_Hm2LLDPAdminStatus_Type())
hm2LLDPAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LLDPAdminStatus.setStatus(_A)
_Hm2LLDPIfTable_Object=MibTable
hm2LLDPIfTable=_Hm2LLDPIfTable_Object((1,3,6,1,4,1,248,11,34,1,1,2))
if mibBuilder.loadTexts:hm2LLDPIfTable.setStatus(_A)
_Hm2LLDPIfEntry_Object=MibTableRow
hm2LLDPIfEntry=_Hm2LLDPIfEntry_Object((1,3,6,1,4,1,248,11,34,1,1,2,1))
hm2LLDPIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hm2LLDPIfEntry.setStatus(_A)
class _Hm2LLDPIfMaxNeighbors_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_Hm2LLDPIfMaxNeighbors_Type.__name__=_B
_Hm2LLDPIfMaxNeighbors_Object=MibTableColumn
hm2LLDPIfMaxNeighbors=_Hm2LLDPIfMaxNeighbors_Object((1,3,6,1,4,1,248,11,34,1,1,2,1,1),_Hm2LLDPIfMaxNeighbors_Type())
hm2LLDPIfMaxNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LLDPIfMaxNeighbors.setStatus(_A)
class _Hm2LLDPIfFDBMode_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('lldpOnly',1),('macOnly',2),('both',3),('autoDetect',4)))
_Hm2LLDPIfFDBMode_Type.__name__=_B
_Hm2LLDPIfFDBMode_Object=MibTableColumn
hm2LLDPIfFDBMode=_Hm2LLDPIfFDBMode_Object((1,3,6,1,4,1,248,11,34,1,1,2,1,2),_Hm2LLDPIfFDBMode_Type())
hm2LLDPIfFDBMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LLDPIfFDBMode.setStatus(_A)
mibBuilder.exportSymbols('HM2-LLDP-MIB',**{'hm2LLDPMib':hm2LLDPMib,'hm2LLDPMibObjects':hm2LLDPMibObjects,'hm2LLDPConfigGroup':hm2LLDPConfigGroup,'hm2LLDPAdminStatus':hm2LLDPAdminStatus,'hm2LLDPIfTable':hm2LLDPIfTable,'hm2LLDPIfEntry':hm2LLDPIfEntry,'hm2LLDPIfMaxNeighbors':hm2LLDPIfMaxNeighbors,'hm2LLDPIfFDBMode':hm2LLDPIfFDBMode})