_C='mandatory'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlUnknowUnicastStormCtrlFastEthernet=ModuleIdentity((1,3,6,1,4,1,4526,17,125))
if mibBuilder.loadTexts:rlUnknowUnicastStormCtrlFastEthernet.setRevisions(('2007-07-04 00:00',))
_RlUnknowUnicastStormCtrlFastEthernetRate_Type=Integer32
_RlUnknowUnicastStormCtrlFastEthernetRate_Object=MibScalar
rlUnknowUnicastStormCtrlFastEthernetRate=_RlUnknowUnicastStormCtrlFastEthernetRate_Object((1,3,6,1,4,1,4526,17,125,1),_RlUnknowUnicastStormCtrlFastEthernetRate_Type())
rlUnknowUnicastStormCtrlFastEthernetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:rlUnknowUnicastStormCtrlFastEthernetRate.setStatus(_C)
class _RlUnknowUnicastStormCtrlFastEthernetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_RlUnknowUnicastStormCtrlFastEthernetStatus_Type.__name__=_A
_RlUnknowUnicastStormCtrlFastEthernetStatus_Object=MibScalar
rlUnknowUnicastStormCtrlFastEthernetStatus=_RlUnknowUnicastStormCtrlFastEthernetStatus_Object((1,3,6,1,4,1,4526,17,125,2),_RlUnknowUnicastStormCtrlFastEthernetStatus_Type())
rlUnknowUnicastStormCtrlFastEthernetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlUnknowUnicastStormCtrlFastEthernetStatus.setStatus(_C)
mibBuilder.exportSymbols('NETGEAR-RADLAN-UUSC-MIB',**{'rlUnknowUnicastStormCtrlFastEthernet':rlUnknowUnicastStormCtrlFastEthernet,'rlUnknowUnicastStormCtrlFastEthernetRate':rlUnknowUnicastStormCtrlFastEthernetRate,'rlUnknowUnicastStormCtrlFastEthernetStatus':rlUnknowUnicastStormCtrlFastEthernetStatus})