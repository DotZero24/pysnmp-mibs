_F='read-create'
_E='aniBsuSubnetConfAddr'
_D='BSUMSUBNETS-MIB'
_C='aniBsuWirelessPort'
_B='BSUWIRELESSIF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bsu,=mibBuilder.importSymbols('ANIROOT-MIB','bsu')
aniBsuWirelessPort,=mibBuilder.importSymbols(_B,_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aniBsuMultSubnets=ModuleIdentity((1,3,6,1,4,1,4325,3,6))
_AniBsuSubnetConfTable_Object=MibTable
aniBsuSubnetConfTable=_AniBsuSubnetConfTable_Object((1,3,6,1,4,1,4325,3,6,1))
if mibBuilder.loadTexts:aniBsuSubnetConfTable.setStatus(_A)
_AniBsuSubnetConfEntry_Object=MibTableRow
aniBsuSubnetConfEntry=_AniBsuSubnetConfEntry_Object((1,3,6,1,4,1,4325,3,6,1,1))
aniBsuSubnetConfEntry.setIndexNames((0,_B,_C),(0,_D,_E))
if mibBuilder.loadTexts:aniBsuSubnetConfEntry.setStatus(_A)
_AniBsuSubnetConfAddr_Type=IpAddress
_AniBsuSubnetConfAddr_Object=MibTableColumn
aniBsuSubnetConfAddr=_AniBsuSubnetConfAddr_Object((1,3,6,1,4,1,4325,3,6,1,1,1),_AniBsuSubnetConfAddr_Type())
aniBsuSubnetConfAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:aniBsuSubnetConfAddr.setStatus(_A)
_AniBsuSubnetConfMask_Type=IpAddress
_AniBsuSubnetConfMask_Object=MibTableColumn
aniBsuSubnetConfMask=_AniBsuSubnetConfMask_Object((1,3,6,1,4,1,4325,3,6,1,1,2),_AniBsuSubnetConfMask_Type())
aniBsuSubnetConfMask.setMaxAccess(_F)
if mibBuilder.loadTexts:aniBsuSubnetConfMask.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'aniBsuMultSubnets':aniBsuMultSubnets,'aniBsuSubnetConfTable':aniBsuSubnetConfTable,'aniBsuSubnetConfEntry':aniBsuSubnetConfEntry,_E:aniBsuSubnetConfAddr,'aniBsuSubnetConfMask':aniBsuSubnetConfMask})