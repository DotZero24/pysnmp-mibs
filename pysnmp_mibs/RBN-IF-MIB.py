_M='rbnIfMIBGroup'
_L='rbnIfHCOutIPv6MulticastPkts'
_K='rbnIfHCInIPv6MulticastPkts'
_J='rbnIfHCOutIPv6Octets'
_I='rbnIfHCInIPv6Octets'
_H='rbnIfHCOutIPv4MulticastPkts'
_G='rbnIfHCInIPv4MulticastPkts'
_F='rbnIfHCOutIPv4Octets'
_E='rbnIfHCInIPv4Octets'
_D='rbnIfEntry'
_C='read-only'
_B='RBN-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifEntry,=mibBuilder.importSymbols('IF-MIB','ifEntry')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnIfMib=ModuleIdentity((1,3,6,1,4,1,2352,2,57))
if mibBuilder.loadTexts:rbnIfMib.setRevisions(('2012-07-18 18:00',))
_RbnIfMIBObjects_ObjectIdentity=ObjectIdentity
rbnIfMIBObjects=_RbnIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,57,0))
_RbnIfTable_Object=MibTable
rbnIfTable=_RbnIfTable_Object((1,3,6,1,4,1,2352,2,57,0,1))
if mibBuilder.loadTexts:rbnIfTable.setStatus(_A)
_RbnIfEntry_Object=MibTableRow
rbnIfEntry=_RbnIfEntry_Object((1,3,6,1,4,1,2352,2,57,0,1,1))
if mibBuilder.loadTexts:rbnIfEntry.setStatus(_A)
_RbnIfHCInIPv4Octets_Type=Counter64
_RbnIfHCInIPv4Octets_Object=MibTableColumn
rbnIfHCInIPv4Octets=_RbnIfHCInIPv4Octets_Object((1,3,6,1,4,1,2352,2,57,0,1,1,1),_RbnIfHCInIPv4Octets_Type())
rbnIfHCInIPv4Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIfHCInIPv4Octets.setStatus(_A)
_RbnIfHCOutIPv4Octets_Type=Counter64
_RbnIfHCOutIPv4Octets_Object=MibTableColumn
rbnIfHCOutIPv4Octets=_RbnIfHCOutIPv4Octets_Object((1,3,6,1,4,1,2352,2,57,0,1,1,2),_RbnIfHCOutIPv4Octets_Type())
rbnIfHCOutIPv4Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIfHCOutIPv4Octets.setStatus(_A)
_RbnIfHCInIPv4MulticastPkts_Type=Counter64
_RbnIfHCInIPv4MulticastPkts_Object=MibTableColumn
rbnIfHCInIPv4MulticastPkts=_RbnIfHCInIPv4MulticastPkts_Object((1,3,6,1,4,1,2352,2,57,0,1,1,3),_RbnIfHCInIPv4MulticastPkts_Type())
rbnIfHCInIPv4MulticastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIfHCInIPv4MulticastPkts.setStatus(_A)
_RbnIfHCOutIPv4MulticastPkts_Type=Counter64
_RbnIfHCOutIPv4MulticastPkts_Object=MibTableColumn
rbnIfHCOutIPv4MulticastPkts=_RbnIfHCOutIPv4MulticastPkts_Object((1,3,6,1,4,1,2352,2,57,0,1,1,4),_RbnIfHCOutIPv4MulticastPkts_Type())
rbnIfHCOutIPv4MulticastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIfHCOutIPv4MulticastPkts.setStatus(_A)
_RbnIfHCInIPv6Octets_Type=Counter64
_RbnIfHCInIPv6Octets_Object=MibTableColumn
rbnIfHCInIPv6Octets=_RbnIfHCInIPv6Octets_Object((1,3,6,1,4,1,2352,2,57,0,1,1,5),_RbnIfHCInIPv6Octets_Type())
rbnIfHCInIPv6Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIfHCInIPv6Octets.setStatus(_A)
_RbnIfHCOutIPv6Octets_Type=Counter64
_RbnIfHCOutIPv6Octets_Object=MibTableColumn
rbnIfHCOutIPv6Octets=_RbnIfHCOutIPv6Octets_Object((1,3,6,1,4,1,2352,2,57,0,1,1,6),_RbnIfHCOutIPv6Octets_Type())
rbnIfHCOutIPv6Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIfHCOutIPv6Octets.setStatus(_A)
_RbnIfHCInIPv6MulticastPkts_Type=Counter64
_RbnIfHCInIPv6MulticastPkts_Object=MibTableColumn
rbnIfHCInIPv6MulticastPkts=_RbnIfHCInIPv6MulticastPkts_Object((1,3,6,1,4,1,2352,2,57,0,1,1,7),_RbnIfHCInIPv6MulticastPkts_Type())
rbnIfHCInIPv6MulticastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIfHCInIPv6MulticastPkts.setStatus(_A)
_RbnIfHCOutIPv6MulticastPkts_Type=Counter64
_RbnIfHCOutIPv6MulticastPkts_Object=MibTableColumn
rbnIfHCOutIPv6MulticastPkts=_RbnIfHCOutIPv6MulticastPkts_Object((1,3,6,1,4,1,2352,2,57,0,1,1,8),_RbnIfHCOutIPv6MulticastPkts_Type())
rbnIfHCOutIPv6MulticastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIfHCOutIPv6MulticastPkts.setStatus(_A)
_RbnIfMIBConformance_ObjectIdentity=ObjectIdentity
rbnIfMIBConformance=_RbnIfMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,57,1))
_RbnIfMIBCompliances_ObjectIdentity=ObjectIdentity
rbnIfMIBCompliances=_RbnIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,57,1,1))
_RbnIfMIBGroups_ObjectIdentity=ObjectIdentity
rbnIfMIBGroups=_RbnIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,57,1,2))
ifEntry.registerAugmentions((_B,_D))
rbnIfEntry.setIndexNames(*ifEntry.getIndexNames())
rbnIfMIBGroup=ObjectGroup((1,3,6,1,4,1,2352,2,57,1,2,1))
rbnIfMIBGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:rbnIfMIBGroup.setStatus(_A)
rbnIfCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,57,1,1,1))
rbnIfCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:rbnIfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnIfMib':rbnIfMib,'rbnIfMIBObjects':rbnIfMIBObjects,'rbnIfTable':rbnIfTable,_D:rbnIfEntry,_E:rbnIfHCInIPv4Octets,_F:rbnIfHCOutIPv4Octets,_G:rbnIfHCInIPv4MulticastPkts,_H:rbnIfHCOutIPv4MulticastPkts,_I:rbnIfHCInIPv6Octets,_J:rbnIfHCOutIPv6Octets,_K:rbnIfHCInIPv6MulticastPkts,_L:rbnIfHCOutIPv6MulticastPkts,'rbnIfMIBConformance':rbnIfMIBConformance,'rbnIfMIBCompliances':rbnIfMIBCompliances,'rbnIfCompliance':rbnIfCompliance,'rbnIfMIBGroups':rbnIfMIBGroups,_M:rbnIfMIBGroup})