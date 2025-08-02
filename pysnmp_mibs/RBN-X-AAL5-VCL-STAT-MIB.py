_N='rbnXAal5VclStatGroup'
_M='current'
_L='rbnXAtmAal5VclOutOctets'
_K='rbnXAtmAal5VclInOctets'
_J='rbnXAtmAal5VclOutPkts'
_I='rbnXAtmAal5VclInPkts'
_H='ifIndex'
_G='IF-MIB'
_F='atmVclVpi'
_E='atmVclVci'
_D='ATM-MIB'
_C='read-only'
_B='RBN-X-AAL5-VCL-STAT-MIB'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmVclVci,atmVclVpi=mibBuilder.importSymbols(_D,_E,_F)
ifIndex,=mibBuilder.importSymbols(_G,_H)
rbnExperiment,=mibBuilder.importSymbols('RBN-SMI','rbnExperiment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnXAal5VclStatMIB=ModuleIdentity((1,3,6,1,4,1,2352,3,1))
_RbnXAal5VclStatMIBObjects_ObjectIdentity=ObjectIdentity
rbnXAal5VclStatMIBObjects=_RbnXAal5VclStatMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,3,1,1))
_RbnXAtmAal5VclStatTable_Object=MibTable
rbnXAtmAal5VclStatTable=_RbnXAtmAal5VclStatTable_Object((1,3,6,1,4,1,2352,3,1,1,1))
if mibBuilder.loadTexts:rbnXAtmAal5VclStatTable.setStatus(_A)
_RbnXAtmAal5VclStatEntry_Object=MibTableRow
rbnXAtmAal5VclStatEntry=_RbnXAtmAal5VclStatEntry_Object((1,3,6,1,4,1,2352,3,1,1,1,1))
rbnXAtmAal5VclStatEntry.setIndexNames((0,_G,_H),(0,_D,_F),(0,_D,_E))
if mibBuilder.loadTexts:rbnXAtmAal5VclStatEntry.setStatus(_A)
_RbnXAtmAal5VclInPkts_Type=Counter32
_RbnXAtmAal5VclInPkts_Object=MibTableColumn
rbnXAtmAal5VclInPkts=_RbnXAtmAal5VclInPkts_Object((1,3,6,1,4,1,2352,3,1,1,1,1,1),_RbnXAtmAal5VclInPkts_Type())
rbnXAtmAal5VclInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnXAtmAal5VclInPkts.setStatus(_A)
_RbnXAtmAal5VclOutPkts_Type=Counter32
_RbnXAtmAal5VclOutPkts_Object=MibTableColumn
rbnXAtmAal5VclOutPkts=_RbnXAtmAal5VclOutPkts_Object((1,3,6,1,4,1,2352,3,1,1,1,1,2),_RbnXAtmAal5VclOutPkts_Type())
rbnXAtmAal5VclOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnXAtmAal5VclOutPkts.setStatus(_A)
_RbnXAtmAal5VclInOctets_Type=Counter32
_RbnXAtmAal5VclInOctets_Object=MibTableColumn
rbnXAtmAal5VclInOctets=_RbnXAtmAal5VclInOctets_Object((1,3,6,1,4,1,2352,3,1,1,1,1,3),_RbnXAtmAal5VclInOctets_Type())
rbnXAtmAal5VclInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnXAtmAal5VclInOctets.setStatus(_A)
_RbnXAtmAal5VclOutOctets_Type=Counter32
_RbnXAtmAal5VclOutOctets_Object=MibTableColumn
rbnXAtmAal5VclOutOctets=_RbnXAtmAal5VclOutOctets_Object((1,3,6,1,4,1,2352,3,1,1,1,1,4),_RbnXAtmAal5VclOutOctets_Type())
rbnXAtmAal5VclOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnXAtmAal5VclOutOctets.setStatus(_A)
_RbnXAal5VclStatMIBConformance_ObjectIdentity=ObjectIdentity
rbnXAal5VclStatMIBConformance=_RbnXAal5VclStatMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,3,1,2))
_RbnXAal5VclStatMIBGroups_ObjectIdentity=ObjectIdentity
rbnXAal5VclStatMIBGroups=_RbnXAal5VclStatMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,3,1,2,1))
_RbnXAal5VclStatMIBCompliances_ObjectIdentity=ObjectIdentity
rbnXAal5VclStatMIBCompliances=_RbnXAal5VclStatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,3,1,2,2))
rbnXAal5VclStatGroup=ObjectGroup((1,3,6,1,4,1,2352,3,1,2,1,1))
rbnXAal5VclStatGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:rbnXAal5VclStatGroup.setStatus(_M)
rbnXAal5VclStatMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,3,1,2,2,1))
rbnXAal5VclStatMIBCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:rbnXAal5VclStatMIBCompliance.setStatus(_M)
mibBuilder.exportSymbols(_B,**{'rbnXAal5VclStatMIB':rbnXAal5VclStatMIB,'rbnXAal5VclStatMIBObjects':rbnXAal5VclStatMIBObjects,'rbnXAtmAal5VclStatTable':rbnXAtmAal5VclStatTable,'rbnXAtmAal5VclStatEntry':rbnXAtmAal5VclStatEntry,_I:rbnXAtmAal5VclInPkts,_J:rbnXAtmAal5VclOutPkts,_K:rbnXAtmAal5VclInOctets,_L:rbnXAtmAal5VclOutOctets,'rbnXAal5VclStatMIBConformance':rbnXAal5VclStatMIBConformance,'rbnXAal5VclStatMIBGroups':rbnXAal5VclStatMIBGroups,_N:rbnXAal5VclStatGroup,'rbnXAal5VclStatMIBCompliances':rbnXAal5VclStatMIBCompliances,'rbnXAal5VclStatMIBCompliance':rbnXAal5VclStatMIBCompliance})