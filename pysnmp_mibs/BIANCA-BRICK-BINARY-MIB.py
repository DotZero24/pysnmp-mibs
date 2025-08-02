_I='binPublicEntIndex'
_H='binFileEntSetId'
_G='binEntIndex'
_F='Integer32'
_E='OctetString'
_D='not-accessible'
_C='BIANCA-BRICK-BINARY-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Ipsec_ObjectIdentity=ObjectIdentity
ipsec=_Ipsec_ObjectIdentity((1,3,6,1,4,1,272,4,26))
_BinTable_Object=MibTable
binTable=_BinTable_Object((1,3,6,1,4,1,272,4,26,65))
if mibBuilder.loadTexts:binTable.setStatus(_A)
_BinEntry_Object=MibTableRow
binEntry=_BinEntry_Object((1,3,6,1,4,1,272,4,26,65,1))
binEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:binEntry.setStatus(_A)
_BinEntIndex_Type=Integer32
_BinEntIndex_Object=MibTableColumn
binEntIndex=_BinEntIndex_Object((1,3,6,1,4,1,272,4,26,65,1,1),_BinEntIndex_Type())
binEntIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:binEntIndex.setStatus(_A)
_BinEntNextIndex_Type=Integer32
_BinEntNextIndex_Object=MibTableColumn
binEntNextIndex=_BinEntNextIndex_Object((1,3,6,1,4,1,272,4,26,65,1,2),_BinEntNextIndex_Type())
binEntNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:binEntNextIndex.setStatus(_A)
_BinEntSetId_Type=Integer32
_BinEntSetId_Object=MibTableColumn
binEntSetId=_BinEntSetId_Object((1,3,6,1,4,1,272,4,26,65,1,3),_BinEntSetId_Type())
binEntSetId.setMaxAccess(_D)
if mibBuilder.loadTexts:binEntSetId.setStatus(_A)
class _BinEntData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BinEntData_Type.__name__=_E
_BinEntData_Object=MibTableColumn
binEntData=_BinEntData_Object((1,3,6,1,4,1,272,4,26,65,1,4),_BinEntData_Type())
binEntData.setMaxAccess(_D)
if mibBuilder.loadTexts:binEntData.setStatus(_A)
_BinFileTable_Object=MibTable
binFileTable=_BinFileTable_Object((1,3,6,1,4,1,272,4,26,66))
if mibBuilder.loadTexts:binFileTable.setStatus(_A)
_BinFileEntry_Object=MibTableRow
binFileEntry=_BinFileEntry_Object((1,3,6,1,4,1,272,4,26,66,1))
binFileEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:binFileEntry.setStatus(_A)
_BinFileEntName_Type=DisplayString
_BinFileEntName_Object=MibTableColumn
binFileEntName=_BinFileEntName_Object((1,3,6,1,4,1,272,4,26,66,1,1),_BinFileEntName_Type())
binFileEntName.setMaxAccess(_B)
if mibBuilder.loadTexts:binFileEntName.setStatus(_A)
_BinFileEntSize_Type=Integer32
_BinFileEntSize_Object=MibTableColumn
binFileEntSize=_BinFileEntSize_Object((1,3,6,1,4,1,272,4,26,66,1,2),_BinFileEntSize_Type())
binFileEntSize.setMaxAccess(_B)
if mibBuilder.loadTexts:binFileEntSize.setStatus(_A)
class _BinFileEntPublic_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_BinFileEntPublic_Type.__name__=_F
_BinFileEntPublic_Object=MibTableColumn
binFileEntPublic=_BinFileEntPublic_Object((1,3,6,1,4,1,272,4,26,66,1,3),_BinFileEntPublic_Type())
binFileEntPublic.setMaxAccess(_B)
if mibBuilder.loadTexts:binFileEntPublic.setStatus(_A)
_BinFileEntSetId_Type=Integer32
_BinFileEntSetId_Object=MibTableColumn
binFileEntSetId=_BinFileEntSetId_Object((1,3,6,1,4,1,272,4,26,66,1,17),_BinFileEntSetId_Type())
binFileEntSetId.setMaxAccess(_B)
if mibBuilder.loadTexts:binFileEntSetId.setStatus(_A)
_BinPublicTable_Object=MibTable
binPublicTable=_BinPublicTable_Object((1,3,6,1,4,1,272,4,26,67))
if mibBuilder.loadTexts:binPublicTable.setStatus(_A)
_BinPublicEntry_Object=MibTableRow
binPublicEntry=_BinPublicEntry_Object((1,3,6,1,4,1,272,4,26,67,1))
binPublicEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:binPublicEntry.setStatus(_A)
_BinPublicEntIndex_Type=Integer32
_BinPublicEntIndex_Object=MibTableColumn
binPublicEntIndex=_BinPublicEntIndex_Object((1,3,6,1,4,1,272,4,26,67,1,1),_BinPublicEntIndex_Type())
binPublicEntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:binPublicEntIndex.setStatus(_A)
_BinPublicEntNextIndex_Type=Integer32
_BinPublicEntNextIndex_Object=MibTableColumn
binPublicEntNextIndex=_BinPublicEntNextIndex_Object((1,3,6,1,4,1,272,4,26,67,1,2),_BinPublicEntNextIndex_Type())
binPublicEntNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:binPublicEntNextIndex.setStatus(_A)
_BinPublicEntSetId_Type=Integer32
_BinPublicEntSetId_Object=MibTableColumn
binPublicEntSetId=_BinPublicEntSetId_Object((1,3,6,1,4,1,272,4,26,67,1,3),_BinPublicEntSetId_Type())
binPublicEntSetId.setMaxAccess(_B)
if mibBuilder.loadTexts:binPublicEntSetId.setStatus(_A)
class _BinPublicEntData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BinPublicEntData_Type.__name__=_E
_BinPublicEntData_Object=MibTableColumn
binPublicEntData=_BinPublicEntData_Object((1,3,6,1,4,1,272,4,26,67,1,4),_BinPublicEntData_Type())
binPublicEntData.setMaxAccess(_B)
if mibBuilder.loadTexts:binPublicEntData.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'bintec':bintec,'bibo':bibo,'ipsec':ipsec,'binTable':binTable,'binEntry':binEntry,_G:binEntIndex,'binEntNextIndex':binEntNextIndex,'binEntSetId':binEntSetId,'binEntData':binEntData,'binFileTable':binFileTable,'binFileEntry':binFileEntry,'binFileEntName':binFileEntName,'binFileEntSize':binFileEntSize,'binFileEntPublic':binFileEntPublic,_H:binFileEntSetId,'binPublicTable':binPublicTable,'binPublicEntry':binPublicEntry,_I:binPublicEntIndex,'binPublicEntNextIndex':binPublicEntNextIndex,'binPublicEntSetId':binPublicEntSetId,'binPublicEntData':binPublicEntData})