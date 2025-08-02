_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fssInterfaces,=mibBuilder.importSymbols('FSS-COMMON-SMI','fssInterfaces')
ifIndex,=mibBuilder.importSymbols(_C,_D)
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fSS_GRE_TUNNEL_INTERFACE=ModuleIdentity((1,3,6,1,4,1,211,1,24,12,700,1000))
if mibBuilder.loadTexts:fSS_GRE_TUNNEL_INTERFACE.setRevisions(('2017-01-12 00:00',))
class UnsignedByte(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class String(TextualConvention,OctetString):status=_A;displayHint='1t'
_Interfaces_stateInterfaceFssGRETable_Object=MibTable
interfaces_stateInterfaceFssGRETable=_Interfaces_stateInterfaceFssGRETable_Object((1,3,6,1,4,1,211,1,24,12,700,1000,1))
if mibBuilder.loadTexts:interfaces_stateInterfaceFssGRETable.setStatus(_A)
_Interfaces_stateInterfaceFssGREEntry_Object=MibTableRow
interfaces_stateInterfaceFssGREEntry=_Interfaces_stateInterfaceFssGREEntry_Object((1,3,6,1,4,1,211,1,24,12,700,1000,1,1))
interfaces_stateInterfaceFssGREEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:interfaces_stateInterfaceFssGREEntry.setStatus(_A)
_Tunnel_stateMTU_Type=Unsigned32
_Tunnel_stateMTU_Object=MibTableColumn
tunnel_stateMTU=_Tunnel_stateMTU_Object((1,3,6,1,4,1,211,1,24,12,700,1000,1,1,1),_Tunnel_stateMTU_Type())
tunnel_stateMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnel_stateMTU.setStatus(_A)
_Tunnel_statePackets_input_Type=Counter64
_Tunnel_statePackets_input_Object=MibTableColumn
tunnel_statePackets_input=_Tunnel_statePackets_input_Object((1,3,6,1,4,1,211,1,24,12,700,1000,1,1,2),_Tunnel_statePackets_input_Type())
tunnel_statePackets_input.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnel_statePackets_input.setStatus(_A)
_Tunnel_stateInput_errors_Type=Counter64
_Tunnel_stateInput_errors_Object=MibTableColumn
tunnel_stateInput_errors=_Tunnel_stateInput_errors_Object((1,3,6,1,4,1,211,1,24,12,700,1000,1,1,3),_Tunnel_stateInput_errors_Type())
tunnel_stateInput_errors.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnel_stateInput_errors.setStatus(_A)
_Tunnel_statePackets_output_Type=Counter64
_Tunnel_statePackets_output_Object=MibTableColumn
tunnel_statePackets_output=_Tunnel_statePackets_output_Object((1,3,6,1,4,1,211,1,24,12,700,1000,1,1,4),_Tunnel_statePackets_output_Type())
tunnel_statePackets_output.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnel_statePackets_output.setStatus(_A)
_Tunnel_stateOutput_errors_Type=Counter64
_Tunnel_stateOutput_errors_Object=MibTableColumn
tunnel_stateOutput_errors=_Tunnel_stateOutput_errors_Object((1,3,6,1,4,1,211,1,24,12,700,1000,1,1,5),_Tunnel_stateOutput_errors_Type())
tunnel_stateOutput_errors.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnel_stateOutput_errors.setStatus(_A)
_Tunnel_stateBytes_Type=Counter64
_Tunnel_stateBytes_Object=MibTableColumn
tunnel_stateBytes=_Tunnel_stateBytes_Object((1,3,6,1,4,1,211,1,24,12,700,1000,1,1,6),_Tunnel_stateBytes_Type())
tunnel_stateBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnel_stateBytes.setStatus(_A)
mibBuilder.exportSymbols('FUJITSU-GRE-TUNNEL-MIB',**{'UnsignedByte':UnsignedByte,'String':String,'fSS-GRE-TUNNEL-INTERFACE':fSS_GRE_TUNNEL_INTERFACE,'interfaces-stateInterfaceFssGRETable':interfaces_stateInterfaceFssGRETable,'interfaces-stateInterfaceFssGREEntry':interfaces_stateInterfaceFssGREEntry,'tunnel-stateMTU':tunnel_stateMTU,'tunnel-statePackets-input':tunnel_statePackets_input,'tunnel-stateInput-errors':tunnel_stateInput_errors,'tunnel-statePackets-output':tunnel_statePackets_output,'tunnel-stateOutput-errors':tunnel_stateOutput_errors,'tunnel-stateBytes':tunnel_stateBytes})