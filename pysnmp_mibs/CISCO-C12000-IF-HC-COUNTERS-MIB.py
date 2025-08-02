_N='ciscoHCCountersMIBGroup'
_M='cHCCounterIfOutUcastPktsLower'
_L='cHCCounterIfOutUcastPktsUpper'
_K='cHCCounterIfOutOctetsLower'
_J='cHCCounterIfOutOctetsUpper'
_I='cHCCounterIfInUcastPktsLower'
_H='cHCCounterIfInUcastPktsUpper'
_G='cHCCounterIfInOctetsLower'
_F='cHCCounterIfInOctetsUpper'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='CISCO-C12000-IF-HC-COUNTERS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoC12000IfHcCountersMIB=ModuleIdentity((1,3,6,1,4,1,9,10,31))
_CHCCounterMIBObjects_ObjectIdentity=ObjectIdentity
cHCCounterMIBObjects=_CHCCounterMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,31,1))
_CHCCounterTable_Object=MibTable
cHCCounterTable=_CHCCounterTable_Object((1,3,6,1,4,1,9,10,31,1,1))
if mibBuilder.loadTexts:cHCCounterTable.setStatus(_A)
_CHCCounterEntry_Object=MibTableRow
cHCCounterEntry=_CHCCounterEntry_Object((1,3,6,1,4,1,9,10,31,1,1,1))
cHCCounterEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cHCCounterEntry.setStatus(_A)
_CHCCounterIfInOctetsUpper_Type=Counter32
_CHCCounterIfInOctetsUpper_Object=MibTableColumn
cHCCounterIfInOctetsUpper=_CHCCounterIfInOctetsUpper_Object((1,3,6,1,4,1,9,10,31,1,1,1,1),_CHCCounterIfInOctetsUpper_Type())
cHCCounterIfInOctetsUpper.setMaxAccess(_C)
if mibBuilder.loadTexts:cHCCounterIfInOctetsUpper.setStatus(_A)
_CHCCounterIfInOctetsLower_Type=Counter32
_CHCCounterIfInOctetsLower_Object=MibTableColumn
cHCCounterIfInOctetsLower=_CHCCounterIfInOctetsLower_Object((1,3,6,1,4,1,9,10,31,1,1,1,2),_CHCCounterIfInOctetsLower_Type())
cHCCounterIfInOctetsLower.setMaxAccess(_C)
if mibBuilder.loadTexts:cHCCounterIfInOctetsLower.setStatus(_A)
_CHCCounterIfInUcastPktsUpper_Type=Counter32
_CHCCounterIfInUcastPktsUpper_Object=MibTableColumn
cHCCounterIfInUcastPktsUpper=_CHCCounterIfInUcastPktsUpper_Object((1,3,6,1,4,1,9,10,31,1,1,1,3),_CHCCounterIfInUcastPktsUpper_Type())
cHCCounterIfInUcastPktsUpper.setMaxAccess(_C)
if mibBuilder.loadTexts:cHCCounterIfInUcastPktsUpper.setStatus(_A)
_CHCCounterIfInUcastPktsLower_Type=Counter32
_CHCCounterIfInUcastPktsLower_Object=MibTableColumn
cHCCounterIfInUcastPktsLower=_CHCCounterIfInUcastPktsLower_Object((1,3,6,1,4,1,9,10,31,1,1,1,4),_CHCCounterIfInUcastPktsLower_Type())
cHCCounterIfInUcastPktsLower.setMaxAccess(_C)
if mibBuilder.loadTexts:cHCCounterIfInUcastPktsLower.setStatus(_A)
_CHCCounterIfOutOctetsUpper_Type=Counter32
_CHCCounterIfOutOctetsUpper_Object=MibTableColumn
cHCCounterIfOutOctetsUpper=_CHCCounterIfOutOctetsUpper_Object((1,3,6,1,4,1,9,10,31,1,1,1,5),_CHCCounterIfOutOctetsUpper_Type())
cHCCounterIfOutOctetsUpper.setMaxAccess(_C)
if mibBuilder.loadTexts:cHCCounterIfOutOctetsUpper.setStatus(_A)
_CHCCounterIfOutOctetsLower_Type=Counter32
_CHCCounterIfOutOctetsLower_Object=MibTableColumn
cHCCounterIfOutOctetsLower=_CHCCounterIfOutOctetsLower_Object((1,3,6,1,4,1,9,10,31,1,1,1,6),_CHCCounterIfOutOctetsLower_Type())
cHCCounterIfOutOctetsLower.setMaxAccess(_C)
if mibBuilder.loadTexts:cHCCounterIfOutOctetsLower.setStatus(_A)
_CHCCounterIfOutUcastPktsUpper_Type=Counter32
_CHCCounterIfOutUcastPktsUpper_Object=MibTableColumn
cHCCounterIfOutUcastPktsUpper=_CHCCounterIfOutUcastPktsUpper_Object((1,3,6,1,4,1,9,10,31,1,1,1,7),_CHCCounterIfOutUcastPktsUpper_Type())
cHCCounterIfOutUcastPktsUpper.setMaxAccess(_C)
if mibBuilder.loadTexts:cHCCounterIfOutUcastPktsUpper.setStatus(_A)
_CHCCounterIfOutUcastPktsLower_Type=Counter32
_CHCCounterIfOutUcastPktsLower_Object=MibTableColumn
cHCCounterIfOutUcastPktsLower=_CHCCounterIfOutUcastPktsLower_Object((1,3,6,1,4,1,9,10,31,1,1,1,8),_CHCCounterIfOutUcastPktsLower_Type())
cHCCounterIfOutUcastPktsLower.setMaxAccess(_C)
if mibBuilder.loadTexts:cHCCounterIfOutUcastPktsLower.setStatus(_A)
_CiscoHCCountersMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoHCCountersMIBNotifications=_CiscoHCCountersMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,31,2))
_CiscoHCCountersMIBConformance_ObjectIdentity=ObjectIdentity
ciscoHCCountersMIBConformance=_CiscoHCCountersMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,31,3))
_CiscoHCCountersMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoHCCountersMIBCompliances=_CiscoHCCountersMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,31,3,1))
_CiscoHCCountersMIBGroups_ObjectIdentity=ObjectIdentity
ciscoHCCountersMIBGroups=_CiscoHCCountersMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,31,3,2))
ciscoHCCountersMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,31,3,2,1))
ciscoHCCountersMIBGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ciscoHCCountersMIBGroup.setStatus(_A)
ciscoHCCountersMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,31,3,1,1))
ciscoHCCountersMIBCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:ciscoHCCountersMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoC12000IfHcCountersMIB':ciscoC12000IfHcCountersMIB,'cHCCounterMIBObjects':cHCCounterMIBObjects,'cHCCounterTable':cHCCounterTable,'cHCCounterEntry':cHCCounterEntry,_F:cHCCounterIfInOctetsUpper,_G:cHCCounterIfInOctetsLower,_H:cHCCounterIfInUcastPktsUpper,_I:cHCCounterIfInUcastPktsLower,_J:cHCCounterIfOutOctetsUpper,_K:cHCCounterIfOutOctetsLower,_L:cHCCounterIfOutUcastPktsUpper,_M:cHCCounterIfOutUcastPktsLower,'ciscoHCCountersMIBNotifications':ciscoHCCountersMIBNotifications,'ciscoHCCountersMIBConformance':ciscoHCCountersMIBConformance,'ciscoHCCountersMIBCompliances':ciscoHCCountersMIBCompliances,'ciscoHCCountersMIBCompliance':ciscoHCCountersMIBCompliance,'ciscoHCCountersMIBGroups':ciscoHCCountersMIBGroups,_N:ciscoHCCountersMIBGroup})