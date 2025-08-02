_D='Integer32'
_C='ifIndex'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ifIndex,=mibBuilder.importSymbols(_B,_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltMesIssDhcpSnoopMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,32))
if mibBuilder.loadTexts:eltMesIssDhcpSnoopMIB.setRevisions(('2022-10-05 00:00',))
_EltMesIssDhcpSnoopObjects_ObjectIdentity=ObjectIdentity
eltMesIssDhcpSnoopObjects=_EltMesIssDhcpSnoopObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,32,1))
_EltMesIssDhcpSnoopGlobals_ObjectIdentity=ObjectIdentity
eltMesIssDhcpSnoopGlobals=_EltMesIssDhcpSnoopGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,32,1,1))
_EltMesIssDhcpSnoopInterfaceConfigs_ObjectIdentity=ObjectIdentity
eltMesIssDhcpSnoopInterfaceConfigs=_EltMesIssDhcpSnoopInterfaceConfigs_ObjectIdentity((1,3,6,1,4,1,35265,1,139,32,1,2))
_EltMesIssDhcpSnoopInterfaceTable_Object=MibTable
eltMesIssDhcpSnoopInterfaceTable=_EltMesIssDhcpSnoopInterfaceTable_Object((1,3,6,1,4,1,35265,1,139,32,1,2,1))
if mibBuilder.loadTexts:eltMesIssDhcpSnoopInterfaceTable.setStatus(_A)
_EltMesIssDhcpSnoopInterfaceEntry_Object=MibTableRow
eltMesIssDhcpSnoopInterfaceEntry=_EltMesIssDhcpSnoopInterfaceEntry_Object((1,3,6,1,4,1,35265,1,139,32,1,2,1,1))
eltMesIssDhcpSnoopInterfaceEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:eltMesIssDhcpSnoopInterfaceEntry.setStatus(_A)
class _EltMesIssDhcpSnoopInterfaceStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_EltMesIssDhcpSnoopInterfaceStatus_Type.__name__=_D
_EltMesIssDhcpSnoopInterfaceStatus_Object=MibTableColumn
eltMesIssDhcpSnoopInterfaceStatus=_EltMesIssDhcpSnoopInterfaceStatus_Object((1,3,6,1,4,1,35265,1,139,32,1,2,1,1,1),_EltMesIssDhcpSnoopInterfaceStatus_Type())
eltMesIssDhcpSnoopInterfaceStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltMesIssDhcpSnoopInterfaceStatus.setStatus(_A)
mibBuilder.exportSymbols('ELTEX-MES-ISS-DHCP-SNOOP-MIB',**{'eltMesIssDhcpSnoopMIB':eltMesIssDhcpSnoopMIB,'eltMesIssDhcpSnoopObjects':eltMesIssDhcpSnoopObjects,'eltMesIssDhcpSnoopGlobals':eltMesIssDhcpSnoopGlobals,'eltMesIssDhcpSnoopInterfaceConfigs':eltMesIssDhcpSnoopInterfaceConfigs,'eltMesIssDhcpSnoopInterfaceTable':eltMesIssDhcpSnoopInterfaceTable,'eltMesIssDhcpSnoopInterfaceEntry':eltMesIssDhcpSnoopInterfaceEntry,'eltMesIssDhcpSnoopInterfaceStatus':eltMesIssDhcpSnoopInterfaceStatus})