_L='ieee8021PfcGlobalReqdGroup'
_K='ieee8021PfcIndications'
_J='ieee8021PfcRequests'
_I='ieee8021PfcLinkDelayAllowance'
_H='ieee8021PfcIfEntry'
_G='read-only'
_F='systemGroup'
_E='SNMPv2-MIB'
_D='ifGeneralInformationGroup'
_C='IF-MIB'
_B='IEEE8021-PFC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ieee802dot1mibs,=mibBuilder.importSymbols('IEEE8021-TC-MIB','ieee802dot1mibs')
ifEntry,ifGeneralInformationGroup=mibBuilder.importSymbols(_C,'ifEntry',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
systemGroup,=mibBuilder.importSymbols(_E,_F)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ieee8021PFCMib=ModuleIdentity((1,3,111,2,802,1,1,21))
if mibBuilder.loadTexts:ieee8021PFCMib.setRevisions(('2018-06-28 00:00','2014-12-15 00:00','2010-02-08 00:00'))
_Ieee8021PfcMIBObjects_ObjectIdentity=ObjectIdentity
ieee8021PfcMIBObjects=_Ieee8021PfcMIBObjects_ObjectIdentity((1,3,111,2,802,1,1,21,1))
_Ieee8021PfcIfTable_Object=MibTable
ieee8021PfcIfTable=_Ieee8021PfcIfTable_Object((1,3,111,2,802,1,1,21,1,1))
if mibBuilder.loadTexts:ieee8021PfcIfTable.setStatus(_A)
_Ieee8021PfcIfEntry_Object=MibTableRow
ieee8021PfcIfEntry=_Ieee8021PfcIfEntry_Object((1,3,111,2,802,1,1,21,1,1,1))
if mibBuilder.loadTexts:ieee8021PfcIfEntry.setStatus(_A)
_Ieee8021PfcLinkDelayAllowance_Type=Unsigned32
_Ieee8021PfcLinkDelayAllowance_Object=MibTableColumn
ieee8021PfcLinkDelayAllowance=_Ieee8021PfcLinkDelayAllowance_Object((1,3,111,2,802,1,1,21,1,1,1,1),_Ieee8021PfcLinkDelayAllowance_Type())
ieee8021PfcLinkDelayAllowance.setMaxAccess('read-write')
if mibBuilder.loadTexts:ieee8021PfcLinkDelayAllowance.setStatus(_A)
_Ieee8021PfcRequests_Type=Counter32
_Ieee8021PfcRequests_Object=MibTableColumn
ieee8021PfcRequests=_Ieee8021PfcRequests_Object((1,3,111,2,802,1,1,21,1,1,1,2),_Ieee8021PfcRequests_Type())
ieee8021PfcRequests.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021PfcRequests.setStatus(_A)
if mibBuilder.loadTexts:ieee8021PfcRequests.setUnits('Requests')
_Ieee8021PfcIndications_Type=Counter32
_Ieee8021PfcIndications_Object=MibTableColumn
ieee8021PfcIndications=_Ieee8021PfcIndications_Object((1,3,111,2,802,1,1,21,1,1,1,3),_Ieee8021PfcIndications_Type())
ieee8021PfcIndications.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021PfcIndications.setStatus(_A)
if mibBuilder.loadTexts:ieee8021PfcIndications.setUnits('Indications')
_Ieee8021PfcConformance_ObjectIdentity=ObjectIdentity
ieee8021PfcConformance=_Ieee8021PfcConformance_ObjectIdentity((1,3,111,2,802,1,1,21,2))
_Ieee8021PfcCompliances_ObjectIdentity=ObjectIdentity
ieee8021PfcCompliances=_Ieee8021PfcCompliances_ObjectIdentity((1,3,111,2,802,1,1,21,2,1))
_Ieee8021PfcGroups_ObjectIdentity=ObjectIdentity
ieee8021PfcGroups=_Ieee8021PfcGroups_ObjectIdentity((1,3,111,2,802,1,1,21,2,2))
ifEntry.registerAugmentions((_B,_H))
ieee8021PfcIfEntry.setIndexNames(*ifEntry.getIndexNames())
ieee8021PfcGlobalReqdGroup=ObjectGroup((1,3,111,2,802,1,1,21,2,2,1))
ieee8021PfcGlobalReqdGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ieee8021PfcGlobalReqdGroup.setStatus(_A)
ieee8021PfcCompliance=ModuleCompliance((1,3,111,2,802,1,1,21,2,1,1))
ieee8021PfcCompliance.setObjects(*((_E,_F),(_C,_D),(_B,_L)))
if mibBuilder.loadTexts:ieee8021PfcCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8021PFCMib':ieee8021PFCMib,'ieee8021PfcMIBObjects':ieee8021PfcMIBObjects,'ieee8021PfcIfTable':ieee8021PfcIfTable,_H:ieee8021PfcIfEntry,_I:ieee8021PfcLinkDelayAllowance,_J:ieee8021PfcRequests,_K:ieee8021PfcIndications,'ieee8021PfcConformance':ieee8021PfcConformance,'ieee8021PfcCompliances':ieee8021PfcCompliances,'ieee8021PfcCompliance':ieee8021PfcCompliance,'ieee8021PfcGroups':ieee8021PfcGroups,_L:ieee8021PfcGlobalReqdGroup})