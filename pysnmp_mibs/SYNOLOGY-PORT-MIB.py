_H='ethPortGroup'
_G='ethPortSpeed'
_F='ethPortStatus'
_E='read-only'
_D='ethPortIndex'
_C='Integer32'
_B='SYNOLOGY-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
synoEthPort=ModuleIdentity((1,3,6,1,4,1,6574,109))
if mibBuilder.loadTexts:synoEthPort.setRevisions(('2020-12-20 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_EthPortTable_Object=MibTable
ethPortTable=_EthPortTable_Object((1,3,6,1,4,1,6574,109,1))
if mibBuilder.loadTexts:ethPortTable.setStatus(_A)
_EthPortEntry_Object=MibTableRow
ethPortEntry=_EthPortEntry_Object((1,3,6,1,4,1,6574,109,1,1))
ethPortEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:ethPortEntry.setStatus(_A)
class _EthPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EthPortIndex_Type.__name__=_C
_EthPortIndex_Object=MibTableColumn
ethPortIndex=_EthPortIndex_Object((1,3,6,1,4,1,6574,109,1,1,1),_EthPortIndex_Type())
ethPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ethPortIndex.setStatus(_A)
class _EthPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('up',2),('down',3)))
_EthPortStatus_Type.__name__=_C
_EthPortStatus_Object=MibTableColumn
ethPortStatus=_EthPortStatus_Object((1,3,6,1,4,1,6574,109,1,1,2),_EthPortStatus_Type())
ethPortStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ethPortStatus.setStatus(_A)
_EthPortSpeed_Type=Gauge32
_EthPortSpeed_Object=MibTableColumn
ethPortSpeed=_EthPortSpeed_Object((1,3,6,1,4,1,6574,109,1,1,3),_EthPortSpeed_Type())
ethPortSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:ethPortSpeed.setStatus(_A)
_EthPortConformance_ObjectIdentity=ObjectIdentity
ethPortConformance=_EthPortConformance_ObjectIdentity((1,3,6,1,4,1,6574,109,2))
_EthPortCompliances_ObjectIdentity=ObjectIdentity
ethPortCompliances=_EthPortCompliances_ObjectIdentity((1,3,6,1,4,1,6574,109,2,1))
_EthPortGroups_ObjectIdentity=ObjectIdentity
ethPortGroups=_EthPortGroups_ObjectIdentity((1,3,6,1,4,1,6574,109,2,2))
ethPortGroup=ObjectGroup((1,3,6,1,4,1,6574,109,2,2,1))
ethPortGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:ethPortGroup.setStatus(_A)
ethPortCompliance=ModuleCompliance((1,3,6,1,4,1,6574,109,2,1,1))
ethPortCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:ethPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'synoEthPort':synoEthPort,'ethPortTable':ethPortTable,'ethPortEntry':ethPortEntry,_D:ethPortIndex,_F:ethPortStatus,_G:ethPortSpeed,'ethPortConformance':ethPortConformance,'ethPortCompliances':ethPortCompliances,'ethPortCompliance':ethPortCompliance,'ethPortGroups':ethPortGroups,_H:ethPortGroup})